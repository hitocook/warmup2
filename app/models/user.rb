class User < ActiveRecord::Base
	validates :username, presence: true, uniqueness: true, length: { maximum: 128 }
	has_secure_password validations: false
	validates :password, length: {maximum: 128}
end
