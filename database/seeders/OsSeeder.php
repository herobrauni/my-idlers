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
        ];

        DB::table('os')->insert($os);
    }
}
