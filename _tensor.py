import torch 

# x=torch.empty(5,3)
# print(x)
x=torch.rand(5,3)
print(x)
# x=torch.zeros(5,3,dtype=torch.long)
# print(x)
# x=torch.tensor([5.5,3])
# print(x)
# x=x.new_ones(5,3,dtype=torch.double)
# print(x)
# x=torch.randn_like(x,dtype=torch.float)
# print(x)
# print(x.size())
# print(x.shape)
# y=torch.rand(5,3)
# print(y)
# print(x+y)
# print(torch.add(x,y))
# result=torch.empty(5,3)
# torch.add(x,y,out=result)
# print(result)
# y=x[0:];
# print(y)
# y+=1;
# print(x)
# y=x.view(15)
# z=x.view(-1,5)
# print(x.size(),y.size(),z.size())
# print(x)
# print(y)
# print(z)
# x_cp=x.clone().view(15)
# x-=1
# print(x)
# print(x_cp)
# x=torch.randn(1)
# print(x.item())
# x=torch.arange(1,3).view(1,2)
# print(x)
# y=torch.arange(1,4).view(3,1)
# print(y)
# print(x+y)
# x=torch.tensor([1,2])
# y=torch.tensor([3,4])
# id_before=id(y)
# y[:]=y+x
# print(id(y)==id_before)

if torch.cuda.is_available():
    device=torch.device("cuda")
    y=torch.ones_like(x,device=device)
    x=x.to(device)
    z=x+y
    print(z)
    print(z.to("cpu",torch.double))
