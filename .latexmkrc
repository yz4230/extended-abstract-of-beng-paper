$biber = 'biber %O %B';
$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
$bibtex = 'bibtex %O %B';  # Note: %B instead of %S is often recommended
$max_repeat = 5;  # Increase number of compilation passes
