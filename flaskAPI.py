from flask import Flask, render_template, request, redirect, url_for
import main
app=Flask(__name__)

@app.route('/')
def button():
    return render_template('button.html')       

@app.route('/Scrap', methods=["POST"])
def Scrap():
    print('Crawling Started')
    main.main()
    return 'Crawling Completed'
    
if __name__=='__main__':
    app.run()