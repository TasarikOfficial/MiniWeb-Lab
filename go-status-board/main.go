package main
import("html/template";"net/http";"time")
var page=template.Must(template.New("p").Parse(`<!doctype html><meta name=viewport content="width=device-width"><style>body{font:16px system-ui;background:#050505;color:#eee;max-width:700px;margin:60px auto;padding:24px}.card{padding:22px;border:1px solid #333;border-radius:18px;background:#111}.ok{color:#30d158}</style><h1>Go Status Board</h1><div class=card><b class=ok>● All systems operational</b><p>Server time: {{.}}</p></div>`))
func main(){http.HandleFunc("/",func(w http.ResponseWriter,r *http.Request){page.Execute(w,time.Now().Format(time.RFC1123))});http.ListenAndServe(":8080",nil)}
