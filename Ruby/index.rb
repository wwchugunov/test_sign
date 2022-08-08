require "openssl"
require "base64"
require "json"

def sign(data)
    private_key = "QP7RZD2IZlMn2Q1yyxDq3wsVe7dGozvWKZyEBB8F"
    # входные данные - хеш
    
    # экранируем url
    json_data = data.to_json.gsub('/', '\/')

    # конвертируем хеш в json-строку и получаем ее в base64, убираем ненужные \n
    base64data = Base64.encode64(json_data).gsub("\n", "")
    # приделываем приватный ключ до и после base64 строки
    concat_base64 = [private_key, base64data, private_key].join
    # получаем бинарный дайджест зашифрованный приватным ключом от объединенной строки и форсим ему кодировку UTF-8
    hash = OpenSSL::HMAC.digest('sha1', private_key, concat_base64).force_encoding("UTF-8")
    # получаем base64 строку из полученного ранее дайджеста, опять убираем ненужные \n
    sign = Base64.encode64(hash).gsub("\n", "")

    # возвращаем исходный хеш данных добавив к нему sign
    data.merge(sign: sign)

end

params = {
  type: "getSession",
  callback: 'http://localhost:3000/payments',
  merchant: "000000020000001",
  tranid: "5",
  ordertype: "3",
  description: "description",
  amount: "477",
  currency: "980",
  clientParams: {
    cardHolderName: "Mr.Cardholder",
    billAddrCity: "Kyiv",
    billAddrCountry: "804",
    billAddrLine3: "",
    billAddrLine2: "",
    billAddrLine1: "test",
    billAddrPostCode: "03201",
    billAddrState: "18",
    billMobilePhone: "380501112233",
    billEmail: "test@gmail.com"
  }
}

json_params = sign(params).to_json.gsub('/', '\/')
puts json_params