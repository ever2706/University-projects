#Creador: Ever Ortega Calderón

#Decidir el número de iteraciones 
Numerodeiteraciones <- 1000000   
#Definicion de las incertidumbres tipicas   

#Diametro modelo

resolDiametro <- runif(Numerodeiteraciones, -0.005,0.005) 
repetDiametro <- rnorm(Numerodeiteraciones, 0 , 0.0709225/sqrt(5)) #hay que dividir entre raiz n?
empDiametro<- runif(Numerodeiteraciones, -0.04 , 0.04)
estimadorDiametro<-120.0360

#Masa modelo 
resolMasa<- runif(Numerodeiteraciones,-0.005,0.005)
repetMasa<- rnorm(Numerodeiteraciones,  0,  0.021908902/sqrt(5) ) #hay que dividir entre raiz n?
certifDiametro <- rnorm(Numerodeiteraciones, 0 , 0.01/2)
estimadorMasa=543.096

#Unión del modelo  
d <- estimadorDiametro + resolDiametro+repetDiametro+empDiametro    
m<- estimadorMasa +resolMasa+repetMasa+certifDiametro

#Calculo Densidad
rho<- (6*m)/(pi * d^3)
incertidumbreDensidad<- sd(rho)
densidad<- mean(rho)

incertidumbreDensidad
densidad

hist(rho, ylab= 'frecuencia', col = 'green', breaks=200, xlab = 'valores')