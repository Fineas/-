use std::{
    process,
    collections::BTreeMap,
};
use serde_json;
use std::path::Path;
use serde::{Serialize, Deserialize};
use move_binary_format::file_format::CompiledModule;
use move_core_types::{account_address::AccountAddress};

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct FnInfo {
    pub is_test: bool,
}

#[derive(Clone, Debug, Eq, Hash, PartialEq, PartialOrd, Ord, Serialize, Deserialize)]
pub struct FnInfoKey {
    pub fn_name: String,
    pub mod_addr: AccountAddress,
}

pub type FnInfoMap = BTreeMap<FnInfoKey, FnInfo>;

fn main() {

    let pid = process::id();
    println!("SUI ID is {}", pid);
    
    let mod_bytes : Vec<u8> = std::fs::read(Path::new(
        "/root/Rust-Sandbox/bytecode_examples/example2/build/example2/bytecode_modules/restricted_transfer.mv" // wrong_module.mv
    )).unwrap();
    // println!("Module Bytes: {:#?}", mod_bytes);

    let compiled_module : CompiledModule = CompiledModule::deserialize(&mod_bytes).unwrap();
    let serialized_compiled_module : &mut Vec<u8> = &mut Vec::new();
    compiled_module.serialize(serialized_compiled_module);
    let serialized_vec = serde_json::to_string(serialized_compiled_module).unwrap();
    // println!("Compiled Module: {:#?}", compiled_module);
    // println!("Serialized Module: {:#?}", serialized_vec);

    let fn_info_map : FnInfoMap = BTreeMap::new();
    let serialized_map = serde_json::to_string(&fn_info_map).unwrap();

    let status = process::Command::new("sandbox")
        .env_remove("SUINDBOX")
        .args(&[serialized_vec])
        // .args(&[serialized_map])
        .arg("3100")
        .arg("50331645")
        .status()
        .expect("failed to execute process");

    println!("Sandbox Output = {:#?}", status);

    assert!(
        status.success(),
        "\nSandbox Failed!\n"
    );
    
}