# -*- coding: utf-8 -*-

"""
Main file. Contains program execution logic.
"""

from __future__ import print_function

import inspect
import sys

from commands import (
    ListCommand,
    NewCommand,
    ExitCommand,
    DoneCommand,
    UndoneCommand,
    UserExitException,
)
from models import (
    Storage,
)
from utils import get_input_function

def get_routes():
    """
    This function contains the dictionary of possible commands.
    :return: `dict` of possible commands, with the format: `name -> class`
    """

    # Dynamic load:
    # def class_filter(klass):
    #     return inspect.isclass(klass) \
    #            and klass.__module__ == BaseCommand.__module__ \
    #            and issubclass(klass, BaseCommand) \
    #            and klass is not BaseCommand
    #
    # routes = inspect.getmembers(
    #     sys.modules[BaseCommand.__module__],
    #     class_filter
    # )
    # return dict((route.label(), route) for _, route in routes)

    return {
        ListCommand.label(): ListCommand,
        NewCommand.label(): NewCommand,
        ExitCommand.label(): ExitCommand,
        DoneCommand.label(): DoneCommand,
        UndoneCommand.label(): UndoneCommand,
    }


def perform_command(command):
    """
    Performs the command by name.
    Stores the result in `Storage()`.
    :param command: command name, selected by user.
    """

    command = command.lower()
    routes = get_routes()

    try:
        command_class = routes[command]
        command_inst = command_class()

        storage = Storage()
        command_inst.perform(storage.items)
    except KeyError:
        print('Bad command, try again.')
    except UserExitException as ex:
        print(ex)
        raise


def parse_user_input():
    """
    Gets the user input.
    :return: `str` with the user input.
    """

    input_function = input

    message = 'Input your command: (%s): ' % '|'.join(
        {
            ListCommand.label(): ListCommand,
            NewCommand.label(): NewCommand,
            ExitCommand.label(): ExitCommand,
            DoneCommand.label(): DoneCommand,
            UndoneCommand.label(): UndoneCommand,
        }.keys()
    )
    return input_function(message)


def main():
    """
    Main method, works infinitelly until user runs `exit` command.
    Or hits `Ctrl+C` in the console.
    """

    while True:
        try:
            command = parse_user_input()
            perform_command(command)
        except UserExitException:
            break
        except Exception as e:
            print('You have done something wrong!', e)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
