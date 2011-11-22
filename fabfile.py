from fabric.api import local

def clean():
    local("rm draft.aux")
    local("rm draft.bbl")
    local("rm draft.blg")
    local("rm draft.log")
    local("rm draft.pdf")
    local("rm fabfile.pyc")

def draft():
    local("pdflatex draft.tex")
    local("bibtex draft")
    local("pdflatex draft.tex")
    local("pdflatex draft.tex")
    

