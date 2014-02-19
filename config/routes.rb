LoginApp::Application.routes.draw do

  root 'users#client'

  match '/users/login', to: 'users#login', via: :post
  match '/users/add',   to: 'users#add',   via: :post
  match '/TESTAPI/resetFixture', to: 'users#TESTAPI_resetFixture', via: :post
  match '/TESTAPI/unitTests',    to: 'users#unitTests', via: :post

end
