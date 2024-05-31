#***# Done #***#
print('Helloworld')
# this is the main file we have to run to initialize the app

from website import create_app
#Importing our custom package named website to create an app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    #Debug = true, needs to  be removed once in production
    