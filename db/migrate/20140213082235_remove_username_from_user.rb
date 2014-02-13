class RemoveUsernameFromUser < ActiveRecord::Migration
  def change
    remove_column :users, :Username, :String
  end
end
