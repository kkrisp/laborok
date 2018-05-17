m=imread("kallibracio.png");
k = m(500,:)'; # horizontal cut, needs to transpone
save("-ascii", "firstcut.data", "k");
k = m(:, 500); # vertical cut, not need to transpone
save("-ascii", "firstcut2.data", "k");