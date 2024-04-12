    def show_genre(self, afishas):
        cursor.execute(f"SELECT genre FROM movies")
        genres=cursor.fetchall()
        genresList=[]
        for i in range(len(genres)):
            genresList.append(genres[i][0])
        genresList=set(genresList)

        i=0
        
        while True:
            cursor.execute(f"SELECT name FROM cinemas WHERE genre = {genresList[i]}")
            cinemas =cursor.fetchall()[0][0]
            cursor.execute(f"SELECT name FROM movies WHERE genre = {genresList[i]}")
            movies =cursor.fetchall()[0][0]
            # print(f'{cursor.fetchall()[0][0]}, Дата и время: {afisha[4]}, {afisha[5]}, Стоимость: {afisha[3]}')
            lst=[]
            for movie in movies:
                lst.append([genresList[i],cinemas, movie])

            print(tabulate([genresList[i],cinema, ], headers=['Genre','Cinema', 'Movie'], tablefmt="grid"))

            i+=1
            if i == 6:
                break
        while True:
            try:
                cinema=int(input('Выбери кинотеатр (введи номер который указан рядом с названием нужного вам кинотеатра от 1 до 5): '))
                if cinema < 1:
                    print("Введи от 1 до 5")
                elif cinema > 5:
                    print("Введи от 1 до 5")
                else:
                    break
            except ValueError:
                print("Введи цифру")
        self.id_cinema=cinema