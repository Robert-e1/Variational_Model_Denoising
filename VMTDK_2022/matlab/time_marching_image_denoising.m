%%% TIME-MARCHING IMAGE DENOISING
%%% Tibor Lukic 2021, Novi Sad
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% load ph_bottle_64_trans; ph_orig=ph_bottle_64_trans;
% 
%   load ph_fish2_64; ph_orig=ph_fish2_64;   
% load ph_shepp_logan; ph_orig=ph_shepp_logan;  % gray image 128x128  6 gray levels 
% load titelski_breg; ph_orig=titelski_breg;
    load csenge_1; ph_orig=csenge_1;
% load aracs_1; ph_orig=aracs_1;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

u_input=ph_orig;
isnr=10;
[u_input,sigma_square]=add_noise(ph_orig,isnr);
u_start=u_input;

% ISOTROPIC DIFFUSION
  %  isotropic_diffusion=true;
% ANISOTROPIC DIFFUSION
    isotropic_diffusion=false;
    
display_progress=1;    


if isotropic_diffusion,
     lambda=0.01/sigma_square; % for isotropic deffusion, IP_11
     delta_t=0.001; % isotropic
else
    lambda=0.16/sigma_square; % for anisotropic deffusion, IP_11
    delta_t=0.0001; % anisotropic
end;


main_stopping_crit=10^(-3);
total_iterations=0;
u_current=u_start;
u_new=u_start;



if display_progress,
    
im_show(u_input);
[m n]=size(u_input);
set(gcf, 'Position', [0.2 2 4.5*(n/m) 4.8]); % figure position and size
title({['Noisy image '  ' SNR=' num2str(snr(ph_orig,u_new)) ]}); 
drawnow;

 
figure; % for solution window 



%set(gcf, 'WindowStyle', 'normal');
% set(gca, 'Unit', 'inches'); 
% set(gca, 'Position', [0 0 4.5*(n/m) 4.5]); % image position and size
 set(gcf, 'Unit', 'inches'); 
 set(gcf, 'Position', [8.4 2 4.5*(n/m) 4.8]); % figure position and size


   % set(gcf, 'Unit', 'inches'); 
   % set(gcf, 'Position', [8.5 1.8 7 5.2]); % figure position and size
     set(gca, 'Unit', 'inches'); 
     set(gca, 'Position', [0 0 4.5*(n/m) 4.5]); % image position and size
     
end;


while ( norm( u_current(:)-u_new(:) ) > main_stopping_crit ) || ( total_iterations<5 ),
    
    u_current=u_new;
    
    if isotropic_diffusion,
         new_diffusion=isotropic_diffusion_EL(u_current);
    else
         new_diffusion=anisotropic_diffusion_EL(u_current);
    end;
    
      u_new=u_current+delta_t*(new_diffusion+lambda*(u_input-u_current));
     
     %[Gx,Gy]=gradient(u_current);
     %GRADIJENT_NORM=Gx.^2+Gy.^2;
     %u_new=u_current-delta_t* GRADIJENT_NORM; % probe
      
    total_iterations=total_iterations+1;
     
    
    if display_progress,   
     imshow(u_new,[0 1],'InitialMagnification','fit');
     title({['Reconstruction ' ' norm=' num2str(norm( u_new - u_current)) ' it=' num2str(total_iterations) ' SNR=' num2str(snr(ph_orig,u_new)) ]});
     drawnow; 
    % for zz=1:1000000, fprintf('delay counter:  %d \n' ,zz ); end; %PROBE 
    end;
       
    
end;
    
  