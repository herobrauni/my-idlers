<?php

namespace Database\Seeders;

use Carbon\Carbon;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class OsSeeder extends Seeder
{
    public function run()
    {
        $os = [
            ["name" => "None", "created_at" => Carbon::now()],
            ["name" => "Debian 12", "created_at" => Carbon::now()],
            ["name" => "Debian 11", "created_at" => Carbon::now()],
            ["name" => "Ubuntu 24.04", "created_at" => Carbon::now()],
            ["name" => "uCore", "created_at" => Carbon::now()],
            ["name" => "Fedora CoreOS", "created_at" => Carbon::now()],
        ];

        DB::table('os')->insert($os);
    }
}
