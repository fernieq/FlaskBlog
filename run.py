#import the function
from flaskblog import create_app
#create the app object
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
