import psycopg2


connection = psycopg2.connect(
    dbname='markets',
    user='team1',
    password=f'12345',
    host='localhost'
)

cursor = connection.cursor()





# 1. Узнайте какие телефоны из Kivano стоят столько же сколько и компьютеры из Sulpak.

#1 Первая задача

cursor.execute("""SELECT
t1.product_name, t2.product_name, t1.price, t2.price
FROM
kivano t1,
sulpak t2
WHERE
t1.price = t2.price and t1.category_id = t2.category_id""")

print(cursor.fetchall())
######################### 2. Узнайте самую последнюю модель Iphone в магазинах. ########################
cursor.execute('''
                select product_name, produsers.created_at from kivano
                join produsers
                on kivano.product_name like '%Iphone%'
                order by produsers.created_at
                ''')
print(cursor.fetchall())
######################### 3. Выведите на экран список всех ноутбуков из sulpak и только тех телефонов которые имеют одинаковую дату выхода с компьютером из таблицы kivano.###### ##################

# 4. Выведите все китайские продукты.

cursor.execute('''select * from produsers where produser_country = 'China';''')

# 5. Напишите запрос, который выводит продукты любого магазина в порядке их добавления.


# 6. Найдите товары, которые есть в kivano но нет в sulpak.
cursor.execute('''
                select * from kivano
                left outer join sulpak
                on kivano.product_name = sulpak.product_name;
                ''')
print(cursor.fetchall())
# # 7. Найдите все товары в магазине sulpak, где компания-производитель содержит букву "m" в имени.
cursor.execute('''
                select sulpak.product_name, sulpak.price, pr.produser_company from sulpak join produsers as pr on pr.producers_id = sulpak.id
                 where
                producers.product_name like '%m%'
                ''')
print(cursor.fetchall())
# 8. Найдите товары, которые есть и в kivano u sulpak.
cursor.execute('''
                select pr.produser_company, s.product_name
                from produsers pr
                join sulpak as s on pr.produser_id = s.item_id
                where pr.produser_company like '%m%';
                ''')
print(cursor.fetchall())
# 9. Найдите китайские товары из kivano, которые в названии содержат "k".
cursor.execute('''
                select * from kivano
                join produsers
                on kivano.produser_id = produsers.produser_id
                where produsers.produser_country = 'China' and kivano.product_name like '%k%'
                ''')
print(cursor.fetchall())
# 10. Найдите самый последний добавленный товар в таблице produsers, и поменяйте компанию на Apple, и страну на kyrgyzstan.




# 11. Нужно объеденить 2 магазина по product_name и вывести на экран имя продукта и его цену из обоих магазинов, однако не факт что в обоих магазинах будут одинаковые товары, поэтому нужно joinить по полной.
# 12. Найдите самый последний японский товар который был добавлен в produsers.
# 13. Напишите запрос, который прибавит 1000 к цене всех продуктов в sulpak.
cursor.execute('''
                UPDATE sulpak SET price = price + 1000
                where item_id = price
                select   *from sulpak
                ''')

# 14. Узнать разницу между самой высокой ценой в sulpak и самой низкой ценой товар в kivano.
# 15. Выведите на экран цены самых дешёвых телефонов из обоих магазинов.
cursor.execute('''
                select sulpak.price, kivano.price  from sulpak, kivano
                order by sulpak.price, kivano.price limit 10;
                ''')

# 16. Удалить все записи где есть NULL в product_name в обоих магазинах.
######################### 17. Все телефоны у которых год меньше 1998 изменить на 2000 (Выполнить с помощью psycopg2).########################
# 18. Acer закрыл свою фабрику в Бразилии после 2012 года и переехал в Германию, у всех записей в produsers где Acer был произведен в Brazil после 2012 поставьте Germany.
# 19. Выведите первые 16 записей без id, из kivano.
# 20. Выведите на экран все product_name которые относятся к категории laptops в kivano.
# 21. Найдите товары в sulpak, цена которых больше среднего на 2000 и меньше средний на 2000
# 22. Найдите product_company, чьи товары дороже среднего в kivano.

cursor.execute('''
                select product_name, price from kivano 
                where price> (select avg(price) from kivano);
                ''')

# 23. Найдите товар который лежит посередине в таблице sulpak.

cursor.execute('''
                select * from sulpak where item_id = (select count(*) /2 from sulpak);
                ''')
print(cursor.fetchall())
# 24. Поменяйте страну на South Korea везде где страна Korea и компания Asus.
cursor.execute('''
                update produsers set produser_country = 'South Korea' 
                where produser_country = 'korea' and produser_company = 'Aser';
                ''')
print(cursor.fetchall())
# 25. В producers поменяйте Nokia на Microsoft везде где у компании Nokia указана страна USA.
print(cursor.fetchall())
cursor.close()
connection.close()