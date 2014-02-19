class User < ActiveRecord::Base
	validates :username, presence: true, uniqueness: true, length: { maximum: 128 }
	validates :password, length: {maximum: 128}
end
