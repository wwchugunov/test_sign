const crypto = require('crypto');


// Исходные данные
let data = '{"type":"getSession","callback":"https://api1262/4358","merchant":"000000020000001","tranid":"5","ordertype":"3","description":"description","amount":"477","currency":"980","clientParams":{"cardHolderName":"Mr.Cardholder","billAddrCity":"Kyiv","billAddrCountry":"804","billAddrLine3":"","billAddrLine2":"","billAddrLine1":"test","billAddrPostCode":"03201","billAddrState":"18","billMobilePhone":"380501112233","billEmail":"test@gmail.com"}}';
// Приватный люч
let key = 'QP7RZD2IZlMn2Q1yyxDq3wsVe7dGozvWKZyEBB8F';
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


