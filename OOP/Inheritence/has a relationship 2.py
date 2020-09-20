class sportsnews:
    def sportsInfo(self):
        print('sports news information')


class moviesnews:
    def movieInfo(self):
        print('movie news information')


class politicalnews:
    def politicsInfo(self):
        print('political news information')


class durganews:
    def __init__(self):
        self.sport = sportsnews()  # creating sportsnews obj and the ref variable is sport
        self.movies = moviesnews()
        self.political = politicalnews()

    def totalnews(self):
        print('welcome to durga news')
        self.sport.sportsInfo()
        self.movies.movieInfo()
        self.political.politicsInfo()


dnews = durganews()
dnews.totalnews()


# second approach
class alaknews:
    def __init__(self, sport, movies, political):
        self.sport = sport
        self.movies = movies
        self.political = political

    def totalnews(self):
        print('welcome to Alak news')
        self.sport.sportsInfo()
        self.movies.movieInfo()
        self.political.politicsInfo()
print("--------------------------------")
sp = sportsnews()
mo = moviesnews()
pol = politicalnews()
anews = alaknews(sp,mo,pol)
anews.totalnews()



