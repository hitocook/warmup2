class UsersController < ApplicationController
	SUCCESS = 1
	ERR_BAD_CREDENTIALS = -1
	ERR_USER_EXISTS = -2
	ERR_BAD_USERNAME = -3
	ERR_BAD_PASSWORD = -4

	MAX_USERNAME_LENGTH = 128
	MAX_PASSWORD_LENGTH = 128


  def client
  end
  
  def add
  	username = params[:user]
  	password = params[:password]
    if username.empty? || username.length > MAX_USERNAME_LENGTH
      render :json => {errCode: ERR_BAD_USERNAME}

  	elsif User.find_by(username:username)
  		render :json => {errCode: ERR_USER_EXISTS}
  	elsif password.length > MAX_PASSWORD_LENGTH
  		render :json => {errCode: ERR_BAD_PASSWORD}
  	else
  		@user = User.new(username: username, password: password, count: 1)
  		@user.save
			render :json => {errCode: SUCCESS, count: @user.count}	
  	end
  end
  
  def login
  	@user = User.find_by_username(params[:user])
    password = params[:password]
    if @user && params[:password].to_s == @user.password.to_s
      @user.count += 1 
      @user.save
      render :json => {errCode: SUCCESS, count: @user.count}
  	else
  		render :json => {errCode: ERR_BAD_CREDENTIALS}
  	end
  end

  def TESTAPI_resetFixture
  	User.destroy_all()
  	render :json => {errCode: SUCCESS}
  end

  def unitTests
  	result = `rspec spec/requests/unit_tests_spec.rb --format documentation > output.txt`
    result = `cat output.txt`
    words  = result.split(" ")
    total_test = words[words.index("examples,") - 1]
    failures   = words[words.index("failures") - 1]

    render :json => { nrFailed: failures.to_i,
              output: result,
              totalTests: total_test.to_i }
  end
  


end
