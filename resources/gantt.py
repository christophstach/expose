"""
GANTT Chart with Matplotlib
Sukhbinder
Inspired from
<div class="embed-theclowersgroup"><blockquote class="wp-embedded-content"><a href="http://www.clowersresearch.com/main/gantt-charts-in-matplotlib/">Gantt Charts in Matplotlib</a></blockquote><script type="text/javascript"><!--//--><![CDATA[//><!--        !function(a,b){"use strict";function c(){if(!e){e=!0;var a,c,d,f,g=-1!==navigator.appVersion.indexOf("MSIE 10"),h=!!navigator.userAgent.match(/Trident.*rv:11./),i=b.querySelectorAll("iframe.wp-embedded-content");for(c=0;c<i.length;c++)if(d=i[c],!d.getAttribute("data-secret")){if(f=Math.random().toString(36).substr(2,10),d.src+="#?secret="+f,d.setAttribute("data-secret",f),g||h)a=d.cloneNode(!0),a.removeAttribute("security"),d.parentNode.replaceChild(a,d)}else;}}var d=!1,e=!1;if(b.querySelector)if(a.addEventListener)d=!0;if(a.wp=a.wp||{},!a.wp.receiveEmbedMessage)if(a.wp.receiveEmbedMessage=function(c){var d=c.data;if(d.secret||d.message||d.value)if(!/[^a-zA-Z0-9]/.test(d.secret)){var e,f,g,h,i,j=b.querySelectorAll('iframe[data-secret="'+d.secret+'"]'),k=b.querySelectorAll('blockquote[data-secret="'+d.secret+'"]');for(e=0;e<k.length;e++)k[e].style.display="none";for(e=0;e<j.length;e++)if(f=j[e],c.source===f.contentWindow){if(f.removeAttribute("style"),"height"===d.message){if(g=parseInt(d.value,10),g>1e3)g=1e3;else if(200>~~g)g=200;f.height=g}if("link"===d.message)if(h=b.createElement("a"),i=b.createElement("a"),h.href=f.getAttribute("src"),i.href=d.value,i.host===h.host)if(b.activeElement===f)a.top.location.href=d.value}else;}},d)a.addEventListener("message",a.wp.receiveEmbedMessage,!1),b.addEventListener("DOMContentLoaded",c,!1),a.addEventListener("load",c,!1)}(window,document);//--><!]]></script><iframe sandbox="allow-scripts" security="restricted" src="http://www.clowersresearch.com/main/gantt-charts-in-matplotlib/embed/" width="600" height="338" title="“Gantt Charts in Matplotlib” — The Clowers Group" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" class="wp-embedded-content"></iframe></div>
"""
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import matplotlib.dates
from matplotlib.dates import WEEKLY, MONTHLY, DateFormatter, rrulewrapper, RRuleLocator
import numpy as np


def _create_date(datetxt):
    """Creates the date"""
    return int(datetxt)


def CreateGanttChart():
    """
        Create gantt charts with matplotlib
        Give file name.
    """
    data = [
        ['#e67e22', 'Planung', 0, 2],
        ['#f39c12', 'Grundlagen', 1, 3],
        ['#16a085', 'Auswahl der Modelle', 2, 4],
        ['#c0392b', 'Implementierung', 4, 7],
        ['#2980b9', 'Training &\nFine-Tuning', 7, 9],
        ['#8e44ad', 'Testen &\nAnalyse', 7, 10],
        ['#34495e', 'Dokumentation', 0, 10]
    ]

    ylabels = []
    customDates = []
    colors = []

    for record in data:
        color, ylabel, startdate, enddate = record
        colors.append(color)
        ylabels.append(ylabel)
        customDates.append([startdate, enddate])

    ilen = len(ylabels)
    pos = np.arange(0.5, ilen * 0.5 + 0.5, 0.5)
    task_dates = {}
    for i, task in enumerate(ylabels):
        task_dates[task] = customDates[i]
    fig = plt.figure(figsize=(20, 8))
    ax = fig.add_subplot(111)
    for i in range(len(ylabels)):
        start_date, end_date = task_dates[ylabels[i]]
        ax.barh((i * 0.5) + 0.5, end_date - start_date, left=start_date, height=0.3, align='center',
                edgecolor='lightgreen', color=colors[i], alpha=0.8
                )

    print(ylabels)
    locsy, labelsy = plt.yticks(pos, ylabels)
    plt.setp(labelsy, fontsize=14)

    ax.set_xticks(range(11))
    ax.grid(color='g', linestyle=':')


    ax.invert_yaxis()
    plt.savefig('gantt.svg')
    plt.show()


if __name__ == '__main__':
    CreateGanttChart()
