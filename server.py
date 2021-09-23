from flask import Flask
from flask import render_template

app = Flask( __name__ )

dictionaryOfSports = {
    'sport1' : 'Football', 
    'sport2' : 'Basketball', 
    'sport3' : 'Tennis', 
    'sport4' : 'Soccer' 
}

listOfSports = [
    {
        'id' : 123,
        'name' : 'Football'
    },
    {
        'id' : 456,
        'name' : 'Basketball'
    },
    {
        'id' : 789,
        'name' : 'Tennis'
    },
    {
        'id' : 555,
        'name' : 'Soccer'
    }
]

sportsList = ['Football', 'Basketball', 'Tennis', 'Soccer']

@app.route( '/home', methods=['GET'] )
def loadHome():
    return render_template( 'index.html', firstName='Alfredo', sportsList=sportsList, listOfSports=listOfSports )


@app.route( '/sports', methods=['GET'] )
def getSports():
    print( "This is executing my first endpoint in the server" )
    return dictionaryOfSports

@app.route( '/sport/<id>', methods=['GET'] )
def getSportById( id ):
    sportID = int( id )
    for sport in listOfSports:
        if sport['id'] == sportID:
            return "The sport of this id is " + sport['name']
    return "There is no sport with that id, try another one"

    #for i in range( 0, len(listOfSports), 1 ):
    #    if listOfSports[i]['id'] == sportID:
    #       return "The sport of this id is " + listOfSports[i]['name']
    
    

if __name__ == "__main__":
    app.run( debug = True )


# BASE URL : http://127.0.0.1:5000/

