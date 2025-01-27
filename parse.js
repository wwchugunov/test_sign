const crypto = require('crypto');


// Исходные данные
let datastr = ;  //Простой обьект
        
        
let data = JSON.stringify(datastr)
// Приватный люч
let key = '46Vz9Vho9w6L9Z!dHY7Qerek6LWPYMfO5H1yIT7hpcuqs';
// Получение исходных данных JSON
let datax = JSON.parse(data);
// Преобразование данных в строку
let data_str = JSON.stringify(datax);
// Экранирование ссылок
data_str  = data_str.replace(/\//g, '\\/')
// Шифрование в base64
let base64data = Buffer.from(data_str, "utf8").toString("base64");
// Конкотенация Ключ, данные, ключ
const concat = key + base64data + key;
// Кодирование sha1
let hmac = crypto.createHmac("sha1", key);
let hash = hmac.update(Buffer.from(concat, 'utf-8')).digest('digest');
let sign = Buffer.from(hash, "utf8").toString("base64");
// Флрмирование sign
let req = JSON.stringify({...datax, ...{sign}});
// Финал
console.log('6 - final request: ', req); 
