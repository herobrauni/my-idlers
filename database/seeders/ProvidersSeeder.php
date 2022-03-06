<?php

namespace Database\Seeders;

use App\Models\Providers;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

class ProvidersSeeder extends Seeder
{
    public function run()
    {

        $providers = [
            ['name' => "Myself"],
            ['name' => "Advin servers"],
            ['name' => "AWS"],
            ['name' => "Bandit Host"],
            ['name' => "Bit Accel"],
            ['name' => "Bluehost"],
            ['name' => "BudgetNode"],
            ['name' => "BuyVM"],
            ['name' => "CloudCone"],
            ['name' => "Cloud Five Limited"],
            ['name' => "Clouvider"],
            ['name' => "Cloudways"],
            ['name' => "CrownCloud"],
            ['name' => "David Froehlich"],
            ['name' => "Dedispec"],
            ['name' => "DesiVPS"],
            ['name' => "Digital Ocean"],
            ['name' => "Domain.com"],
            ['name' => "Dr. Server"],
            ['name' => "DreamHost"],
            ['name' => "Dynadot"],
            ['name' => "Evolution Host"],
            ['name' => "ExonHost"],
            ['name' => "ExtraVM"],
            ['name' => "FlowVPS"],
            ['name' => "FreeRangeCloud"],
            ['name' => "George Data Center"],
            ['name' => "Gestiondbi"],
            ['name' => "Godaddy"],
            ['name' => "Gullo's Hosting"],
            ['name' => "HappyBeeHost"],
            ['name' => "Hetzner"],
            ['name' => "Host Sailor"],
            ['name' => "HostEons"],
            ['name' => "HostGator"],
            ['name' => "HostHatch"],
            ['name' => "Hostcram"],
            ['name' => "Hostigger"],
            ['name' => "Hostinger"],
            ['name' => "HostMaxim"],
            //['name' => "HostSolutions"],
            ['name' => "HostUS"],
            ['name' => "HostYD"],
            //['name' => "Hotlineservers"],
            ['name' => "Hover"],
            ['name' => "Hyonix"],
            ['name' => "Hyperexpert"],
            ['name' => "Inception Hosting"],
            ['name' => "Incognet"],
            ['name' => "IndoVirtue"],
            ['name' => "IOflood"],
            ['name' => "IonSwitch"],
            ['name' => "Khan Web Host"],
            ['name' => "KTS24 (Haendler.IT)"],
            ['name' => "LaunchVPS"],
            ['name' => "LETBox"],
            ['name' => "Lilchosting"],
            ['name' => "Linode"],
            ['name' => "Liteserver"],
            ['name' => "lkwebhosting"],
            ['name' => "MrVM"],
            ['name' => "MYW"],
            ['name' => "Namecheap"],
            ['name' => "NameSilo"],
            ['name' => "Naranjatech"],
            ['name' => "NexusBytes"],
            ['name' => "Novos"],
            ['name' => "One Provider"],
            ['name' => "OVH"],
            ['name' => "Owned networks"],
            ['name' => "Porkbun"],
            ['name' => "Prolo"],
            ['name' => "Pure Voltage"],
            ['name' => "Quantum Core"],
            ['name' => "Quick Packet"],
            ['name' => "RackNerd"],
            ['name' => "Rad Web hosting"],
            ['name' => "RamNode"],
            ['name' => "ReadyDedis"],
            ['name' => "ResellerClub"],
            ['name' => "Servarica"],
            ['name' => "Servers Galore"],
            ['name' => "Shock Hosting"],
            ['name' => "Skylon Host"],
            ['name' => "SmallWeb"],
            ['name' => "Smarthost"],
            ['name' => "SpryServers"],
            ['name' => "SSDBlaze"],
            ['name' => "Store Host"],
            ['name' => "TeraSwitch"],
            ['name' => "Terrahost"],
            ['name' => "Ulayer"],
            ['name' => "Ultra VPS"],
            ['name' => "Virmach"],
            ['name' => "VPS Aliens"],
            ['name' => "Vultr"],
            ['name' => "WebHorizon"],
            ['name' => "Wishhosting"],
            ['name' => "X4B"],
            ['name' => "ZeptoVM"]
        ];

        DB::table('providers')->insert($providers);
    }
}
