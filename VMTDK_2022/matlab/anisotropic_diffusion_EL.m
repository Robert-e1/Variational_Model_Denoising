function D=anisotropic_diffusion_EL(u)
 % u - image in matrix form
 
[Gx,Gy]=gradient(u);

% [Gx,Gy]=gradient_function(u);

imgradient_magnitude=sqrt(Gx.^2+Gy.^2)+0.0000001;

% if imgradient_magnitude<0.000001, imgradient_magnitude=0.000001; end;

D=divergence(Gx./imgradient_magnitude,Gy./imgradient_magnitude);

