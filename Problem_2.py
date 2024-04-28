'''
Time Complexity = O(u*s)
Space Complexity = O(u*s)

Works on Leetcode
'''
class FavoriteGenre:
    def getFavoriteGenre(self, genreSongs, usersSongs):
        songGenre = {}
        usersGenres = {}
        for genre in genreSongs:
            songList = genreSongs.get(genre)
            for song in songList:
                #store the genre for every song in a hashMap
                songGenre[song] = genre
        
        
        for user in usersSongs:
            #get list of songs for user
            songList = usersSongs.get(user)
            genreCount = {}
            maxCount = 0
            favGenres = []
            for song in songList:
                #get genre for every song and maintain genre count in a hashMap
                song_genre = songGenre.get(song)
                genreCount[song_genre] = genreCount.get(song_genre, 0) + 1
                #also calculate the max Count
                maxCount = max(maxCount, genreCount.get(song_genre))
            #find Genre with maxCount and append the genre to the user favorite genres
            for genre in genreCount:
                if genreCount.get(genre) == maxCount:
                    favGenres.append(genre)
            usersGenres[user] = favGenres
        return usersGenres
    
f =  FavoriteGenre()
genreSongs = {}
genreSongs["pop"] = [8,1,6]
genreSongs["rock"] = [3,5,2,9]
genreSongs["classical"] = [4,7,10]

usersSongs = {}
usersSongs["A"] = [4,1,6,8]
usersSongs["B"] = [2,4,9,10]
usersSongs["C"] = [8,3,9,4]
usersSongs["D"] = [1,9,8,6,7]

print(f.getFavoriteGenre(genreSongs, usersSongs))
                    
            