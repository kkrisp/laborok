middle = 484;

# cutting callibration picture
m=imread("kallibracio.png");
k = m(middle,:)';
save("-ascii", "cut_kallib.data", "k");

# cutting data picture
names = ["mA150.png";"mA170.png";"mA190.png";"mA210.png";"mA230.png";"mA520.png";"mA570.png";"mA620.png";"mA670.png";"mA720.png"];
for i = 1:10
    m=imread(names(i,:));
    k = m(middle,:)';
    name = names(i,1:5);
    name = ["cut_", name, ".data"];
    save("-ascii", name, "k");
end