require 'spec_helper'

describe User do

	before do
		@user = User.new(username: "user0", password: "password")
	end

	subject { @user }

	it { should respond_to(:user1) }
	it { should respond_to(:password) }
	it { should respond_to(:count)  }
	it { should be_valid }
	
	describe "when username is duplicate" do
		before do
			user_with_same_name = @user.dup
			user_with_same_name.save
		end

		it { should_not be_valid }
	end

	describe "when username is empty" do
		before { @user. username= "" }
		it { should_not be_valid }
	end

	describe "when username and password are very long but valid" do
		before do
			@user.username = "verylongusername" * 8
			@user.password = "verylongpassword" * 8
		end

		it { should be_valid }		
	end	

	describe "when username is valid but password is not present" do
		before do
			@user.username = "user1"
			@user.password = ""
		end
		it { should be_valid}
	end

	describe "when username >128" do
		before { @user.username = "a" * 129 }
		it { should_not be_valid }
	end

	describe "when password >128" do
		before do
			@user.username = "user0"
			@user.password = "a" * 129
		end

		it { should_not be_valid }
	end


	after(:each) do
  		User.delete_all
	end

end
