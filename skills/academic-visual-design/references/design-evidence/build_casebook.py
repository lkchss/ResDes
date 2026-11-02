"""Original synthetic teaching examples; not benchmark data or publication reproductions."""
from pathlib import Path
import json
import html
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'casebook'
OUT.mkdir(exist_ok=True)
data={
 'synthetic':True,
 'purpose':'Illustrative design cases, not empirical validation or benchmark fixtures',
 'models':['Unadjusted','Baseline adjusted','Site adjusted'],
 'rows':[{'term':'Outreach','estimate':[.042187,.039714,.041931],'se':[.008692,.008411,.008765]},
         {'term':'Peer support','estimate':[.025734,.023491,.021226],'se':[.007911,.008032,.008174]}],
 'n':[842,835,821],
 'small_effects':[{'group':'A','difference_proportion':.000123},{'group':'B','difference_proportion':.000186}],
 'paired':{'unit':'Synthetic response score','before':[30,45,25,60,50,35],'after':[38,54,36,67,60,44]},
 'effects':[{'name':'A','estimate':.32,'lower':.12,'upper':.52},
            {'name':'B','estimate':.28,'lower':-.04,'upper':.60},
            {'name':'C','estimate':.21,'lower':.14,'upper':.28}],
 'effect_interval':'Supplied illustrative 95% confidence intervals for standardized mean differences; not calculated from the paired example'
}
(OUT/'data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path'})

before=np.array(data['paired']['before']);after=np.array(data['paired']['after'])
fig,axs=plt.subplots(1,2,figsize=(10,4.2),layout='constrained',sharey=True)
axs[0].bar([0,1],[before.mean(),after.mean()],color=['#777777','#0072B2'],width=.52)
for x,y in enumerate([before.mean(),after.mean()]):axs[0].text(x,y+2,f'{y:.1f}',ha='center')
axs[0].set_title('Group means',loc='left',weight='bold')
for a,b in zip(before,after):axs[1].plot([0,1],[a,b],color='#777777',lw=1,alpha=.8,zorder=1)
axs[1].scatter(np.zeros(len(before)),before,color='#555555',s=32,zorder=2)
axs[1].scatter(np.ones(len(after)),after,color='#0072B2',s=32,zorder=2)
axs[1].set_title('The same six participants, connected',loc='left',weight='bold')
for ax in axs:
 ax.set(xticks=[0,1],xticklabels=['Before','After'],xlim=(-.5,1.5),ylim=(0,80),ylabel='Response score')
fig.savefig(OUT/'paired.png',dpi=160);fig.savefig(OUT/'paired.svg');plt.close(fig)

fig,ax=plt.subplots(figsize=(6.4,3.4),layout='constrained')
es=data['effects']; y=np.arange(len(es))
for yy,e in zip(y,es):
 ax.errorbar(e['estimate'],yy,xerr=[[e['estimate']-e['lower']],[e['upper']-e['estimate']]],fmt='o',color='#0072B2',capsize=4,lw=1.8)
ax.axvline(0,color='#777777',lw=1,ls='--')
ax.set(yticks=y,yticklabels=[e['name'] for e in es],ylim=(2.5,-.5),xlim=(-.12,.68),xlabel='Standardized mean difference (95% CI)',ylabel='Intervention')
fig.savefig(OUT/'intervals.png',dpi=160);fig.savefig(OUT/'intervals.svg');plt.close(fig)

def regression(digits):
 s='<table><caption>Retention differences across specifications</caption><thead><tr><th scope="col">Term</th>'+''.join(f'<th scope="col">{m}</th>' for m in data['models'])+'</tr></thead><tbody>'
 for row in data['rows']:
  s+=f'<tr><th scope="row">{row["term"]}</th>'+''.join(f'<td>{v:.{digits}f}<br><span class="se">({se:.{digits}f})</span></td>' for v,se in zip(row['estimate'],row['se']))+'</tr>'
 s+='<tr><th scope="row">Observations</th>'+''.join(f'<td>{n}</td>' for n in data['n'])+'</tr></tbody></table>'
 return s

effect_table='<table><caption>Intervention estimates</caption><thead><tr><th scope="col">Intervention</th><th scope="col">Estimate</th><th scope="col">95% CI</th></tr></thead><tbody>'+''.join(f'<tr><th scope="row">{e["name"]}</th><td>{e["estimate"]:.2f}</td><td>[{e["lower"]:.2f}, {e["upper"]:.2f}]</td></tr>' for e in es)+'</tbody></table>'
precision_table='<table><caption>When three decimals erase the result</caption><thead><tr><th scope="col">Group</th><th scope="col">Source proportion difference</th><th scope="col">Lossy three-decimal display</th><th scope="col">Difference per 10,000</th></tr></thead><tbody>'+''.join(f'<tr><th scope="row">{e["group"]}</th><td>{e["difference_proportion"]:.6f}</td><td class="lossy">{e["difference_proportion"]:.3f}</td><td>{e["difference_proportion"]*10000:.2f}</td></tr>' for e in data['small_effects'])+'</tbody></table>'

page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Academic design casebook</title>
<style>
:root{font-family:system-ui,Arial,sans-serif;color:#182329;background:#f5f3ef;line-height:1.5}*{box-sizing:border-box}body{margin:0}main{max-width:1260px;margin:auto;padding:40px 30px}h1{font-size:32px;line-height:1.15}h2{font-size:23px;margin:0 0 18px}h3{font-size:16px;margin:0 0 12px}nav{display:flex;gap:18px;flex-wrap:wrap;margin:26px 0}a{color:#005a82}section{padding:28px;background:white;border:1px solid #d8d8d2;margin:24px 0;scroll-margin-top:20px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}table{border-collapse:collapse;width:100%;font-family:Georgia,'Times New Roman',serif;font-size:15px;font-variant-numeric:lining-nums tabular-nums}caption{text-align:left;font-weight:bold;padding:0 0 12px}thead{border-top:1.5px solid #222;border-bottom:1px solid #666}tbody{border-bottom:1.5px solid #222}th,td{padding:10px 8px;vertical-align:top}th{text-align:left}thead th:not(:first-child),td{text-align:right}tbody th{font-weight:normal}.se{color:#43505a}.lossy{background:#fff1df}img{width:100%;height:auto;display:block}.notes{font-size:14px;max-width:95ch}footer{font-size:13px;margin:28px 0} @media(max-width:850px){.pair{grid-template-columns:1fr}main{padding:20px 12px}section{padding:20px 12px}.scroll{overflow-x:auto}table{min-width:460px}}@media print{body{background:white}nav{display:none}section{break-inside:avoid;border:0;padding:12px 0}main{padding:0}}
</style><main><h1>Academic design casebook</h1>
<p>Original synthetic teaching examples. These illustrate decisions and their limits; they are not benchmark results or reproduced publication figures.</p>
<nav aria-label="Examples"><a href="#precision">Display precision</a><a href="#small">Small effects</a><a href="#paired">Paired observations</a><a href="#intervals">Lookup or comparison</a></nav>
<section id="precision"><h2>1. Match precision to the comparison</h2><div class="pair"><div class="scroll"><h3>Full precision in every cell</h3>REG6</div><div class="scroll"><h3>Three decimals for this reading task</h3>REG3</div></div>
<p class="notes">Question: how stable are the estimates across specifications? Entries are synthetic differences in retention probability; standard errors appear in parentheses. For this illustrative task, sub-0.001 distinctions are not the target. The shorter display retains the visible pattern and keeps full precision in the source. It is not a rule that all coefficients need three decimals, nor a declaration that source precision is scientifically justified.</p></section>
<section id="small"><h2>2. Simplification can erase evidence</h2><div class="scroll">SMALL</div><p class="notes">Here, the small difference is the point. The three-decimal column is intentionally lossy: it makes two nonzero values look like zero. An explicitly labeled conversion to differences per 10,000 retains the distinction without long decimal strings. The numerical conversion is exact; interpreting these differences still requires study context and uncertainty, which are not supplied in this arithmetic-only example.</p></section>
<section id="paired"><h2>3. Match the figure to the unit of comparison</h2><a href="paired.png"><img src="paired.png" alt="Two views of six synthetic paired observations. Group means rise from 40.8 to 49.8. Connected observations show that all six participants increase, by 7 to 11 score points. Both panels use a 0 to 80 vertical scale."></a><p class="notes">Question: did the same participants change? Group means answer an aggregate question but do not reveal pairing. Connecting the actual matched observations exposes within-person change. Both panels use the same scale. No significance claim is made; six synthetic pairs are not evidence of an intervention effect. With many participants, consider a distribution of changes or another legible paired summary.</p></section>
<section id="intervals"><h2>4. Exact lookup and interval comparison are different tasks</h2><div class="pair"><div class="scroll">EFFECTS</div><a href="intervals.png"><img src="intervals.png" alt="Point estimates and supplied 95 percent confidence intervals: A 0.32, interval 0.12 to 0.52; B 0.28, interval minus 0.04 to 0.60; C 0.21, interval 0.14 to 0.28. The axis has a reference at zero."></a></div><p class="notes">Both views contain the same estimate and interval information. The table supports exact lookup; aligned marks expose relative interval widths and locations. These are illustrative standardized mean differences, unrelated to the paired data above. Interval overlap is not a general test of pairwise differences; do not declare a winning intervention from this graphic.</p></section>
<footer><a href="data.json">Full synthetic data</a> · <a href="../design-context.md">Decision context</a> · <a href="../root-sources.json">Research sources and limits</a><p>Examples are original design synthesis. The literature supports task-sensitive design; it does not empirically validate these particular examples. Source code: <a href="../build_casebook.py">build_casebook.py</a>.</p></footer></main></html>'''
page=page.replace('REG6',regression(6)).replace('REG3',regression(3)).replace('SMALL',precision_table).replace('EFFECTS',effect_table)
(OUT/'index.html').write_text(page,encoding='utf-8')
# Assertions cover the counterexample and the claims in the accessible description.
assert np.all(after>before) and int((after-before).min())==7 and int((after-before).max())==11
assert round(float(before.mean()),1)==40.8 and round(float(after.mean()),1)==49.8
assert all(f"{x['difference_proportion']:.3f}"=='0.000' for x in data['small_effects'])
assert all(e['lower']<=e['estimate']<=e['upper'] for e in es)
print(json.dumps({'casebook':str(OUT/'index.html'),'cases':4,'synthetic':True,'assertions':'passed'}))
