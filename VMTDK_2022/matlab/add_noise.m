function [u_noisy, sigma_square]=add_noise(u,isnr_value)

% u - original image
% isnr_value - initial signal to noise ratio
      
u=double(u);    

sigma_square=sqrt(10^(-isnr_value/10)*var(u(:))); % sigma is the standard deviation of the added noise

noise=randn(size(u)).*sigma_square; 
u_noisy=u+noise; % add noise

while abs( isnr_value - snr(u,u_noisy) )>10^(-4),
    noise=randn(size(u)).*sigma_square; 
    u_noisy=u+noise; % add noise
end;


              
           
        






