# Anonymous lettering for Light IT portal based on RSA

### Lettering flow:
1. Юзер генерирует пару ключей (приватный и публичный)
2. В форму отправки вводит вопрос руководителю, публичный ключ и кодовое слово
(необходимо, что бы при получении ответа определить и вытащить только свое письмо, а не получать все письма и пытаться по очереди расшифровывать)
3. Вопрос и публичный ключ шифруются публичным ключом руководителя, который должен быть на фронтенде или приходить с бекенда.
Вопрос+ключ зашифрованном виде и кодовое слово сохраняются в базе.
4. Когда руководитель хочет ответить на вопрос - он заходит на специальную страницу, видимую только ему,
ввести свой приватный ключ, после чего полученные вопросы могут быть им расшифрованны (все сразу или по запросу)
5. Руководитель выбирает вопрос на который хочет ответить, вводит ответ, который, после этого, шифруется публичным ключем который был отправлен вместе с вопросом.
6. Юзер, переодически должен заходить на форму проверки ответа. На ней он вводит кодовое слово, приватный ключ и если ответ пришел - то он расшифровывается этим приватным ключем.

### Notes:
1. От codeword можно запросто избавиться. Как способ идентификации "какое ответ - какому юзеру" можно использовать id сохраненного письма (т.е. заставлять юзера его запоминать), но codeword просто более user-friendly.
Так же можно просить пользователя вводить только свой приватный ключ, получать все ответы и пытаться расшифровывать по очереди, но это долго.
2. Решение на чистом RSA накладывает некоторые ограничения. Так как длинна шифрируемой информации не может быть длиннее публичного ключа,
то ключи босса, желательно, должны быть сгенерированы 8192 битовыми, что бы юзер мог ввести больше символов в вопросе. Так же, в таком случае, ключи юзера должны быть сгенерированы меньшими чем ключи босса,
так как публичный ключ юзера мы тоже добавляем в шифруемое сообщение (paranoia). И, тогда, ответ руководителя не может быть длинне ключа юзера.
Это проблема, на которую было обращено внимение уже на последнем этапе разработки, поэтому это решение было реализовано до конца.
**Но в этом репозитории есть другая ветка - "pgp", в который шифрование реализовано с помощью PGP, которое не имеет ограничений по размеру cooбщений**

### TO DO
1. Now you can't send messages without js. We need to make no-js forms for those ones who want encrypt/decrypt messages by himself and not use curl.
2. Improve UI.

### Tips for paranoiacs
1. Use https or .onion mirror. Someone can replace boss public key in server response.
2. Don't trusts scripts on page. Better perform all encrypting/decrypting operations by yourself. Now you can use curl for this.
3. Better to use .onion instead https, this will enforce your anonimity.
4. Use Tor Browser. Because someone can make fingerprint of your browser.
5. Everyone knows it: keep you private key like your balls.
6. For every question-answer use new keypair.
7. When you delete old keypair, erase memory region with special tools. Usual deletion just deletes pointer.
8. Don't enter tor without vpn. Don't connect to vpn from your home. You shout order vpn only for bitcoins. That bitcoins must be mixed.
12. Don't trust anyone, including youself.