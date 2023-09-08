syms t y
p=0.001773;
q=0.114767;
f=(1-y)*(p+q*y);
a=0;
b=100;
w0=0;
M=2083.822;

analiF(1)=w0;
for i=1:1:b
  analiF(i+1)= M*((p*(exp((p+q)*i)-1))/(p*(exp((p+q)*i))+q));
endfor
for n=1:100
  if n==5
    
    tic 
    [mTaylor3] = Taylor3 (f,a,b,w0,n);
    
    for i=1:n+1
      mTaylor3(i,2)=M* mTaylor3(i,2);
    endfor  
    tiempo5Taylor3=toc
    
    tic 
    [mRK2] = RK2 (f,a,b,w0,n);
    
    for i=1:n+1
      mRK2(i,2)=M* mRK2(i,2);
    endfor 
    tiempo5RK2=toc
    
    tic 
    [mEuler] = Euler (f,a,b,w0,n);
    for i=1:n+1
      mEuler(i,2)= M*mEuler(i,2);
    endfor  
    tiempo5Euler=toc
    
    figure(1)
    plot (mTaylor3(:,1),mTaylor3(:,2),'g-');
    xlabel('Meses');
    ylabel('Cantidad de productos');
    
    hold on
    plot (mRK2(:,1),mRK2(:,2),'k*--');
    plot (mEuler(:,1),mEuler(:,2),'r:o');
    plot ([0:1:100]',analiF','m'),title('Métodos de aproximación para n=5');
    legend({'g- = Taylor3','k*-- = RK2','r:o=Euler','m=Analítica'},'Location','northwest');
    hold off
    grid
    tiempo5=tiempo5Euler+tiempo5RK2+tiempo5Taylor3
  elseif n==10
    
    tic 
    [mTaylor3] = Taylor3 (f,a,b,w0,n);
    for i=1:n+1
      mTaylor3(i,2)=M* mTaylor3(i,2);
    endfor  
    tiempo10Taylor3=toc
    tic 
    [mRK2] = RK2 (f,a,b,w0,n);
    for i=1:n+1
      mRK2(i,2)=M* mRK2(i,2);
    endfor  
    tiempo10RK2=toc
    tic 
    [mEuler] = Euler (f,a,b,w0,n);
    for i=1:n+1
      mEuler(i,2)= M*mEuler(i,2);
    endfor 
    tiempo10Euler=toc
    figure(2)
    plot (mTaylor3(:,1),mTaylor3(:,2),'g-');
    xlabel('Meses');
    ylabel('Cantidad de productos');
    hold on
    plot (mRK2(:,1),mRK2(:,2),'k*--');
    plot (mEuler(:,1),mEuler(:,2),'r:o');
    plot ([0:1:100]',analiF','m'),title('Métodos de aproximación para n=10');
    legend({'g- = Taylor3','k*-- = RK2','r:o=Euler','m=Analítica'},'Location','northwest');
    hold off
    grid
    tiempo10=tiempo10Euler+tiempo10RK2+tiempo10Taylor3
    
  elseif n==30
    
    tic 
    [mTaylor3] = Taylor3 (f,a,b,w0,n);
    for i=1:n+1
      mTaylor3(i,2)=M* mTaylor3(i,2);
    endfor  
    tiempo30Taylor3=toc
    tic 
    [mRK2] = RK2 (f,a,b,w0,n);
    for i=1:n+1
      mRK2(i,2)=M* mRK2(i,2);
    endfor  
    tiempo30RK2=toc
    tic 
    [mEuler] = Euler (f,a,b,w0,n);
    for i=1:n+1
      mEuler(i,2)= M*mEuler(i,2);
    endfor  
    tiempo30Euler=toc
    figure(3)
    plot (mTaylor3(:,1),mTaylor3(:,2),'g-');
    xlabel('Meses');
    ylabel('Cantidad de productos');
    hold on
    plot (mRK2(:,1),mRK2(:,2),'k*--');
    plot (mEuler(:,1),mEuler(:,2),'r:o');
    plot ([0:1:100]',analiF','m'),title('Métodos de aproximación para n=30');
    legend({'g- = Taylor3','k*-- = RK2','r:o=Euler','m=Analítica'},'Location','northwest');
    hold off
    grid
    tiempo30=tiempo30Euler+tiempo30RK2+tiempo30Taylor3
    
  elseif n==100
    
    tic 
    [mTaylor3] = Taylor3 (f,a,b,w0,n);
    for i=1:n+1
      mTaylor3(i,2)=M* mTaylor3(i,2);
    endfor  
    tiempo100Taylor3=toc
    tic 
    [mRK2] = RK2 (f,a,b,w0,n);
    for i=1:n+1
      mRK2(i,2)=M* mRK2(i,2);
    endfor  
    tiempo100RK2=toc
    tic 
    [mEuler] = Euler (f,a,b,w0,n);
    for i=1:n+1
      mEuler(i,2)= M*mEuler(i,2);
    endfor  
    tiempo100Euler=toc
    figure(4)
    plot (mTaylor3(:,1),mTaylor3(:,2),'g-');
    xlabel('Meses');
    ylabel('Cantidad de productos');
    hold on
    plot (mRK2(:,1),mRK2(:,2),'k*--');
    plot (mEuler(:,1),mEuler(:,2),'r:o');
    plot ([0:1:100]',analiF','m'),title('Métodos de aproximación para n=100');
    legend({'g- = Taylor3','k*-- = RK2','r:o=Euler','m=Analítica'},'Location','northwest');
    hold off
    grid
    tiempo100=tiempo100Euler+tiempo100RK2+tiempo100Taylor3
  else
    continue
  endif
  
  endfor