users3 = {
	"Amy": {
		"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4
	},
	"Ben": {
		"Taylor Swift": 5, "PSY": 2
	},
 	"Clara": {
 		"PSY": 3.5, "Whitney Houston": 4
 		},
 	"Daisy": {
 		"Taylor Swift": 5, "Whitney Houston": 3
 		}
 	}

users2 = {
	"Angelica": {
		"Blues Traveler": 3.5, "Broken Bells": 2.0,
        	"Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5,
 		"The Strokes": 2.5, "Vampire Weekend": 2.0
 		},
 	"Bill": {
 		"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0,
 		"Phoenix": 2.0, "Slightly Stoopid": 3.5,
 		"Vampire Weekend": 3.0
 		},
 	"Chan": {
 		"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0,
 		"Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0
 		},
 	"Dan": {
 		"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5,
 		"Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0,
 		"Vampire Weekend": 2.0
 		},
 	"Hailey": {
 		"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0,
 		"The Strokes": 4.0, "Vampire Weekend": 1.0
 		},
 	"Jordyn": {
 		"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0,
 		"Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0,
 		"Vampire Weekend": 4.0
 		},
 	"Sam": {
 		"Blues Traveler": 5.0, "Broken Bells": 2.0,
 		"Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0,
 		"The Strokes": 5.0
 		},
 	"Veronica": {
 		"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0,
 		"Slightly Stoopid": 2.5, "The Strokes": 3.0
 		}
 	}



def computeDeviations(data):
    deviations={}
    frequency={}
    for bands in data.values():
        for (artist,rating) in bands.items():
            deviations.setdefault(artist,{})
            frequency.setdefault(artist,{})
            for (artist2,rating2) in bands.items():
                if artist2 != artist:
                    frequency[artist].setdefault(artist2, 0.0)
                    frequency[artist][artist2]+=1

                    deviations[artist].setdefault(artist2, 0.0)
                    deviations[artist][artist2]+= (rating-rating2)

    for (item,ratings) in deviations.items():
    	for item2 in ratings:
    	    deviations[item][item2]= deviations[item][item2]/frequency[item][item2] 


    return deviations,frequency

def prediction(user,users2):
	summation=0
	freq=0
	deviations, frequency= computeDeviations(users2)
	recommend={}
	#recommend.setdefault(artist,None)
	for (userItem,userRating) in user.items():
		for(diffItem,diffRating) in deviations.items():

			if diffItem not in user:
				summation+=(deviations[diffItem][userItem]+ userRating)* frequency[diffItem][userItem]
				freq+= frequency[diffItem][userItem]
				recommend.setdefault(diffItem,0.0)
				recommend[diffItem]=summation/freq
	#recommend.sort(lambda x: reverse=True)
	#recommend.sort(key=lambda artistTuple: artistTuple[1], reverse = True)
	return recommend

result=prediction(users2['Sam'], users2)
#result.sorted(key=lambda artist:artist[1], reverse=True)
print (result)



