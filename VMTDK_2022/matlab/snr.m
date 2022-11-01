function  r= snr(u,u_r)

 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 % Signal-To-Noise Ratio (SNR) 
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
 % u   -  original image
 % u_r - reconstructed image
 
 % fprintf('SNR'); 
  
 u_mean=mean(u(:));
 
 r=10*log10( sum( (u(:)-u_mean).^2 ) / sum( (u(:)-u_r(:)).^2 )  );
 
 % END