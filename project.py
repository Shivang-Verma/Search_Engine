import Search_Engine
import Query
from flask import Flask, render_template, redirect, request, jsonify, app

app = Flask(__name__)
search_engine_object = Search_Engine.Search_Engine()
query_object = Query.Query(search_engine_object)

class User:
    search_engine_object = None
    query_object = None

    def __init__(self, se, qe):
        self.search_engine_object = se
        self.query_object = qe

def get_var():
    user = User(search_engine_object, query_object)
    return user

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')

def get_sample(title, rank):
    str = '''< span id = "cover-outer" style = 'border-radius: 19px' >< div id = "cover-inner" style = 'border-radius: 19px' >< div >< div > {{Title}} < / div >< div > Rank: {{Rank}} < / div >< / div >< / div >< / span >'''
    str = str.replace('{{Title}}', title)
    str = str.replace('{{Rank}}', rank)
    return str

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        user = get_var()
        query = request.args.get('query')

        sorted_s_rank, sorted_p_rank = user.query_object.do_query(query)

        str_sorted_p = "<ol>"
        str_sorted_s = "<ol>"
        if len(sorted_p_rank) > 0:
            for rank, value in enumerate(sorted_p_rank, 1):
                temp = "<li>"
                temp += value[0] + "</li>"
                str_sorted_p += temp

        if len(sorted_s_rank) > 0:
            for rank, value in enumerate(sorted_s_rank, 1):
                temp = "<li>"
                temp += value[0] + "</li>"
                str_sorted_s += temp
        str_sorted_p += "</ol>"
        str_sorted_s += "</ol>"
        data = "<div>All Text Appears in: " + str_sorted_p + "</div><br><br><div>Some Text Appear in: " + str_sorted_s + "</div>"
        # data = {'str_sorted_p' : str_sorted_p, 'str_sorted_s': str_sorted_s}
        return data

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=11080)