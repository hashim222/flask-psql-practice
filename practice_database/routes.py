from flask import render_template, request, redirect, url_for
from practice_database import app, db
from practice_database.models import EnterdData


@app.route("/")
def home_page():
    view_database = EnterdData.query.order_by(EnterdData.input_data)
    return render_template('home_page.html', view_database=view_database)


@app.route("/input_page", methods=['GET', 'POST'])
def input_page():
    if request.method == 'POST':
        insert_database = EnterdData(input_data=request.form.get('input_data'))
        db.session.add(insert_database)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('input_page.html')



