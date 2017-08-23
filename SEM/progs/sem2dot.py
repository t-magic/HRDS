#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os
import re

# semのファイル(out_file)を読み込んで、dot形式に変換し、ファイル(dot_file)に書き出す。
def sem2dot_file(latent_list, out_file, dot_file, back_only = True):
    out_str_list = codecs.open(out_file, 'r', encoding='cp932').read().split('\n')
    dot_str_list = sem2dot_list(latent_list, out_str_list, back_only = back_only)
    with codecs.open(dot_file, 'w', encoding='utf8') as f:
        for line in dot_str_list:
            f.write(line + '\n')

# gawkの代わりのもので、semのファイルを読み込んでリスト化したものを入力として、dot形式の
# リストを出力するもの
# sem2dot_fileから呼び出される。
def sem2dot_list(latent_list, out_str_list, back_only = True):
    i = 0
    result_list = []
    result_list.append("digraph  fit {")
    result_list.append("rankdir=TB;")
    result_list.append("size=\"8,8\";")
    result_list.append("edge [fontname=\"sans\"  ,fontsize=8,arrowsize = 0.8,penwidth=0.8];")
    result_list.append("graph [ordering = out,splines = true,overlap = false];")
    result_list.append("center=1;")
    #' '.join(latent_list)
    result_list.append("node [shape =ellipse];{0};".format(' '.join(latent_list)))
    result_list.append("node [fontname=\"serif\" ,fontsize=14, shape=box];")
    result_list.append("{rank=min };")

    for L in out_str_list:
        #print('++ L = {0}'.format(L))
        S = [x.strip() for x in L.split(' ')]
        try:
            S.remove('')
        except:
            pass

        #print('++ S = {0}'.format(S))
        if len(S) >= 5:
            if S[1] == "=~":
                if not back_only:
                    result_list.append('{0}->{1}{2}{3}{4}'.format(S[0], S[2], S[3], S[4], S[5]))
            elif S[1] == "~":
                result_list.append('{0}->{1}{2}{3},dir=back{4}'.format(S[0], S[2], S[3], S[4], S[5]))
            elif S[1] == "~~":
                if not back_only:
                    result_list.append('{0}->{1}{2}{3},dir=both{4}'.format(S[0], S[2], S[3], S[4], S[5]))
            elif S[1] == "~1":
                i = i + 1
                result_list.append('{0}->切片i{1}{2},dir=back{4}'.format(S[0], S[2], S[3], S[4]))
    result_list.append("}")
    return result_list

def select_latency_items(latency_R_Source, encoding='cp932'):
    latency_list0 = []
    r_source_list = codecs.open(latency_R_Source, 'r', encoding=encoding).read().split('\n')
    # r_source_list
    for line in r_source_list:
        items = re.match('#', line)
        if items == None:
            # print(line)
            items2 = re.match('(.+?)=~', line)
            if items2 != None:
                # print(items2.group(1))
                latency_list0.append(items2.group(1).strip())
    return latency_list0

# Graphvizでdotファイルをsvgファイルにする。
def dot2svg(dot_file, latency_list, dot_path, suffix = '', back_only = False):
    svg_file = dot_file.replace('.dot', '') + '.svg'
    png_file = dot_file.replace('.dot', '') + '.png'
    #dot_path = '"C:/Program Files (x86)/Graphviz2.38/bin/dot"'
    if back_only:
        graph_type = 'dot'
    else:
        graph_type = 'twopi'
    os.system('{0} -K{1} -Tsvg {2} -o {3}'.format(dot_path, graph_type, dot_file, svg_file))
    os.system('{0} -K{1} -Tpng {2} -o {3}'.format(dot_path, graph_type, dot_file, png_file))

def out2svg(out_file, latency_list, dot_path, suffix = '', back_only = False):
    dot_file = out_file + suffix + '.dot'
    sem2dot_file(latency_list, out_file, dot_file, back_only = back_only)
    svg_file = dot_file.replace('.dot', '') + '.svg'
    png_file = dot_file.replace('.dot', '') + '.png'
    #dot_path = '"C:/Program Files (x86)/Graphviz2.38/bin/dot"'
    if back_only:
        graph_type = 'dot'
    else:
        graph_type = 'twopi'
    os.system('{0} -K{1} -Tsvg {2} -o {3}'.format(dot_path, graph_type, dot_file, svg_file))
    os.system('{0} -K{1} -Tpng {2} -o {3}'.format(dot_path, graph_type, dot_file, png_file))