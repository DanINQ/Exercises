'use strict';


// + Напишите программу, которая считает площадь прямоугольника, спрашивая у пользователя длину двух сторон

function SquareCalc (a,b) {
	if (typeof(a)==='number' && typeof(b)==='number') {
	return a*b;
	}
}



// + Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-". В зависимости от знака выводит их сумму или разницу

function calc (a, b, sign) {
	if (sign==='+') {return a+b;} else if (sign==='-') {return a-b;} else {return 'wrong args';} 
}



// + Напишите программу, которая находит все простые числа между 0 и пользовательским числом

function SimpleNumCheck (number) {
	for (let num = 2; num <= number; num++) {
		let result = true
		for (let i = 2; i < num; i++) {
			if (num % i == 0) {
				result = false;
				break;
			}
		}
		if (result===true) {
			console.log(num)
		}
	}
}



// + Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами

function DivByFive (a, b) {
	for (let num = a; num <= b; num++) {
		if (num % 5 === 0) {
			console.log(num);
		}
	}
}



// + Создать лист из 6 любых чисел. Отсортировать его по возрастанию

var SomeList = [6,2,56,1,98,18];

SomeList.sort(function (a, b) {
	return a - b
})



// + Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно

var NewDict = {
	3:'f',
	4:'g',
	5:'5b',
	8:'8a',
	14:'1e4',
}

for (let key in NewDict) {
	console.log(key, NewDict[key])
}



// + Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

var NewArr = [12,43,6,12,990,3];

var min = Math.min.apply(null, NewArr);
var max = Math.max.apply(null, NewArr);



// + Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'
 
var LocationArr = ['Earth', 'Russia', 'Moscow'];
var joined = '';
for (let word in LocationArr) {
	joined += LocationArr[word] += (word != 2) ? ' -> ':''
}



// + Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'

var Str = '/bin:/usr/bin:/usr/local/bin';

var NewStr = Str.split(':');



// + Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет

for (let num = 1; num <= 100; num++) {
	if (num % 7 === 0) {console.log(num)}
}



// + Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

var matrix = [
	[3, 45, 67, 3],
	[45, 7, 2, 21],
	[7, 45, 98, 3],
	];

for (string in matrix) {
	console.log(matrix[string])
}

for (let i = 0; i <= 3; i++) {
	for (let string in matrix) {
		console.log(matrix[string][i])
	}
}



// + Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

var WintSoldPassword = ['Желание', 'Ржавый', 17, 'Рассвет', 'Печь', 9, 'Добросердечный', 'Возвращение на родину', 1, 'Товарный вагон'];


for (item in WintSoldPassword) {
	console.log(WintSoldPassword[item], item)
}



// + Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

var OtherArr = ['some value', true, 'to-delete', 'other', 'to-delete', 12, 'also', 'to-delete'];

for (let index = 0; index <= OtherArr.length; index++) {
	if (OtherArr[index] === 'to-delete') {
		OtherArr.splice(index, 1)
	}
}


// + Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль

for (let num = 10; num > 0; num--) {
	console.log(num)
}