class AddCountToUsers < ActiveRecord::Migration
  def change
    add_column :users, :count, :int
  end
end
