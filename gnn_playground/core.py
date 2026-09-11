import math
def train_demo(layers=2, learning_rate=.1, epochs=20):
    layers=max(1,min(5,int(layers))); epochs=max(1,min(200,int(epochs)))
    target=[.2,.8,.35,.9,.6]; weights=[.5]*5; history=[]
    edges=[(0,1),(1,2),(2,3),(0,4)]
    for e in range(epochs):
        propagated=weights[:]
        for _ in range(layers):
            nxt=propagated[:]
            for a,b in edges: nxt[b]=(propagated[b]+propagated[a])/2
            propagated=nxt
        loss=sum((w-t)**2 for w,t in zip(propagated,target))/len(target)
        history.append(round(loss,6))
        rate=float(learning_rate)/(1+0.15*(layers-1))
        weights=[w+rate*(t-w) for w,t in zip(propagated,target)]
    return {'config':{'layers':layers,'learning_rate':float(learning_rate),'epochs':epochs},'history':history,'predictions':[round(w,4) for w in weights]}
def render_html(result):
    pts=','.join(f'{i*70+40},{260-v*220:.1f}' for i,v in enumerate(result['history']))
    bars=''.join(f'<div class="bar" style="height:{v*180+4:.1f}px" title="{v}"></div>' for v in result['predictions'])
    return f'''<!doctype html><meta charset="utf-8"><title>GNN Playground</title><style>body{{font:16px system-ui;max-width:900px;margin:30px auto;color:#172033}}svg{{width:100%;background:#f6f8fb}}.bar{{display:inline-block;width:48px;background:#5b6ee1;margin:4px;vertical-align:bottom}}</style><h1>GNN Playground</h1><p>layers={result['config']['layers']} · learning rate={result['config']['learning_rate']} · epochs={result['config']['epochs']}</p><h2>Training loss</h2><svg viewBox="0 0 900 280"><polyline fill="none" stroke="#e05a47" stroke-width="3" points="{pts}"/></svg><h2>Node predictions</h2><div style="height:200px">{bars}</div>'''

def main(argv=None):
    import argparse, json
    p=argparse.ArgumentParser(); p.add_argument('--layers',type=int,default=2); p.add_argument('--learning-rate',type=float,default=.1); p.add_argument('--epochs',type=int,default=20); p.add_argument('-o','--output',default='gnn-playground.html'); a=p.parse_args(argv)
    r=train_demo(a.layers,a.learning_rate,a.epochs); open(a.output,'w',encoding='utf8').write(render_html(r)); print(json.dumps(r,ensure_ascii=False,indent=2)); return 0
