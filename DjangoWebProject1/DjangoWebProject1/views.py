
# -*- coding:utf-8 -*-
from django.shortcuts import render
from . import disco
def fun1(request):
    someThing=disco.diffusion()
    return  render(request,"index.html",{'getSomeThings':someThing})