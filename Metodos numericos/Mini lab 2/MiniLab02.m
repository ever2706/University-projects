cantpts=0;
energAcumul=[];
veloAcumul=[];
for i=1:1:25
  if i==3 
    cantpts=3;
    
    
  elseif i==10
    cantpts=10;
    
    
  elseif i==16;
    cantpts=16;
    
    
  elseif i==25;
    cantpts=25;
  else
    continue
  endif
  pkg load image
  img=imread ('BordeDeformacionClio.PNG');
  imshow(img);
  [Wi,Xi]=ginput(cantpts);
  Wi
  Xi
  Fxi=[]
  m1=(1.623-1.218)/(Wi(length(Wi))-Wi(1));
  b1=-m1*(Wi(1))+1.218;
  m2=(1.198)/((Xi(length(Xi)))-(Xi(1)));
  b2=-m2*(Xi(length(Xi)))+1.198;
  Wires=0;
  Xires=0;
  for i=1:1:length(Wi)
    Wires(i)=m1*Wi(i)+b1;
  endfor
  for i=1:1:length(Xi)
    Xires(i)=m2*Xi(i)+b2;
  endfor
  Wires
  Xires
  
  for i=1:1:length(Xires)
    Fxi(i)=-69733.622*Xires(i)+(962670.18*(Xires(i))^2)/2;
  endfor
  M=[Wires;Fxi]' 
  Trapecioseq(M);
  V=sqrt((2*Trapecioseq(M))/915)
  Vkm=(V/1000)*3600
  energAcumul(end+1)=Trapecioseq(M)
  veloAcumul(end+1)=Vkm
  
endfor
puntos=[3,10,16,25];
figure(1);
plot(puntos,energAcumul),title("Cantidad de puntos vs energía absorbida");
grid;
figure(2);
plot(puntos,veloAcumul),title("Cantidad de puntos vs velocidad del vehículo en km/h");
grid;