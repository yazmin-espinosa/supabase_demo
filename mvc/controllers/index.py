import web

render = web.template.render('mvc/views', base='template')

class Index: 
    def GET(self, *args):
        return render.index() 
    