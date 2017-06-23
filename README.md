# Anonymous lettering for Light IT portal based on PGP

### Lettering flow:
1. Юзер генерирует пару ключей (приватный и публичный)
2. В форму отправки вводит вопрос руководителю, публичный ключ и кодовое слово
(необходимо, что бы при получении ответа определить и вытащить только свое письмо, а не получать все письма и пытаться по очереди расшифровывать)
3. Вопрос и публичный ключ шифруются публичным ключом руководителя, который должен быть на фронтенде или приходить с бекенда.
Вопрос+ключ зашифрованном виде и кодовое слово сохраняются в базе.
4. Когда руководитель хочет ответить на вопрос - он заходит на специальную страницу, видимую только ему,
ввести свой приватный ключ и пароль от него, после чего полученные вопросы могут быть им расшифрованны (все сразу или по запросу)
5. Руководитель выбирает вопрос на который хочет ответить, вводит ответ, который, после этого, шифруется публичным ключем который был отправлен вместе с вопросом.
6. Юзер, переодически должен заходить на форму проверки ответа. На ней он вводит кодовое слово, приватный ключ, пароль от него и если ответ пришел - то он расшифровывается этим приватным ключем.

### Notes:
1. От codeword можно запросто избавиться. Как способ идентификации "какое ответ - какому юзеру" можно использовать id сохраненного письма (т.е. заставлять юзера его запоминать), но codeword просто более user-friendly.
Так же можно просить пользователя вводить только свой приватный ключ, получать все ответы и пытаться расшифровывать по очереди, но это долго.
2. Решение на PGP не накладывает ограничений на размер сообщений. Но, PGP ключи гененрировать сложнее, и при их генерации необходимо указывать имя и емеил - это может сбить юзера с толку (но их можно заполнить рандомно).
Есть несколько выходов, если это не устраивает.
2.1 Можно немного переделать текущую реализацию так, что бы PGP ключи использовались только руководителем, т.е. юзер сможет указывать самые обычные RSA при задавании вопроса / получении ответа, а шифроваться вопрос будет PGP ключом руководителя.
Так длина пользовательского сообщения будет неограниченной, но возможная длинна ответа руководителя будет зависить от того, какого размера ключ указал пользователь.
2.2 Написать свою пародию на PGP, в которой не нужно будет вводить email и name. Но тогда в базе нужно будет хранить еще зашифрованный пароль от зашифрованного вопроса и зашифрованный пароль от зашифрованного ответа.

### Tips for paranoiacs
1. Use https or .onion mirror. Someone can replace boss public key in server response.
2. Don't trusts scripts on page. Better perform all encrypting/decrypting operations by yourself. Now you can use curl for this.
3. Better to use .onion instead https, this will enforce your anonimity.
4. Use Tor Browser. Because someone can make fingerprint of your browser.
5. For every question-answer use new keypair.
6. When you delete old keypair, erase memory region with special tools. Usual deletion just deletes pointer.
7. Don't enter tor without vpn. Don't connect to vpn from your home. You shout order vpn only for bitcoins. That bitcoins must be mixed.
