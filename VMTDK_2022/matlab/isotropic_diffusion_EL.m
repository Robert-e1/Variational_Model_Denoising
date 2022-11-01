function D=isotropic_diffusion_EL(u)
 % u - image in matrix form
 
[Gx,Gy]=gradient(u);

D=divergence(Gx,Gy);

