from flask import Flask, request, redirect, render_template_string
app=Flask(__name__); links=[]
PAGE="""<!doctype html><meta name=viewport content='width=device-width'><title>Link Saver</title><style>body{font:16px system-ui;max-width:680px;margin:60px auto;padding:20px;background:#09090b;color:#fafafa}form,li{display:flex;gap:10px;padding:14px;background:#18181b;border-radius:14px;margin:10px 0}input{flex:1;padding:12px;border-radius:9px;border:0}button{background:#0a84ff;color:white;border:0;border-radius:9px;padding:0 18px}a{color:#64d2ff}</style><h1>Link Saver</h1><form method=post><input name=title placeholder=Title required><input name=url placeholder=https:// required><button>Save</button></form>{% for x in links %}<li><a href='{{x.url}}'>{{x.title}}</a></li>{% endfor %}"""
@app.route("/",methods=["GET","POST"])
def home():
 if request.method=="POST": links.append({"title":request.form["title"],"url":request.form["url"]}); return redirect("/")
 return render_template_string(PAGE,links=links)
if __name__=="__main__": app.run(debug=True)
