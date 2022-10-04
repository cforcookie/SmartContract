pragma solidity <=0.8.7; 
 
contract A { 
 
    struct Transfer { 
        uint id;
        address giver;
        address taker;
        uint value;
        uint code;
        string catigory;
        string dyscription;
        uint time;
        bool status;
    }

    struct Confirm_admin {
        uint id;
        uint id_transfer;
        address admin;
        bool status_admin;
    }
    
    struct Shablon { 
        string catigory;
        uint value;
    }

    struct Vote {
        uint id;
        address from;
        address[] givers;
        bool status;
    }

    mapping(uint => string) public shablon_name;
    mapping(uint => Shablon[]) public shablon_info;

    mapping(address => bool) public user_rule;
    mapping(address => bool) public user;
    address[] public admins;

    uint shablon_lenght;
    Vote[] public votes;
    Transfer[] public transfers;
    Confirm_admin[] public confirm_admin;

    mapping(uint => bool) public info_used;
    mapping(uint => uint) public info_id;

    constructor () {
        user_rule[0x9925DC2679EE571256829c69E354c45F93523424] = true;
        user[0x9925DC2679EE571256829c69E354c45F93523424] = true;
        admins.push(0x9925DC2679EE571256829c69E354c45F93523424);
        shablon_name[shablon_lenght] = "Present";
        shablon_info[shablon_lenght].push(Shablon("Self to self", 30));
        shablon_info[shablon_lenght].push(Shablon("Self to self", 50));
        shablon_info[shablon_lenght].push(Shablon("Self to self", 70));
        shablon_lenght++;
    }

    function register() public {
        require(user[msg.sender] == false, "You allready in system");
        user[msg.sender] = true;
    }
 
    function create_transfer(address taker, uint value, uint code, string memory catigory,  
    string memory dyscription) public payable {
        require(msg.sender != taker, "You can't send money to yourself"); 
        require(msg.sender.balance > value, "Value less"); 
        require(view_value(value, false) == true, "Value less");
        transfers.push(Transfer(transfers.length, msg.sender, taker, value, code, catigory, dyscription, block.timestamp, false)); 
        msg.value;
    }

    function create_transfer_safe(address taker, uint value, uint code, string memory catigory,  
    string memory dyscription, address admin) public payable {
        require(msg.sender != taker, "You can't send money to yourself"); 
        require(msg.sender.balance > value, "Value less");
        require(view_value(value, true) == true, "Value less");
        uint id = transfers.length;
        uint id2 = confirm_admin.length;
        transfers.push(Transfer(id, msg.sender, taker, value, code, catigory, dyscription, block.timestamp, false));
        confirm_admin.push(Confirm_admin(id2, id, admin, false));
        info_used[id] = true;
        info_id[id] = id2;
        msg.value;
    }

    function view_value(uint value, bool status) private view returns(bool) {
        if (status == true) {
            if (msg.value == value + value/100*10) {
                return(true);
            }
            else {
                return(false);
            }
        }
        else {
            if (msg.value == value) {
                return(true);
            }
            else {
                return(false);
            }
        }
    }

    function confirm_transfer(uint id) public payable {
        require(confirm_admin[id].admin == msg.sender, "Not for you");
        require(transfers[confirm_admin[id].id_transfer].giver != msg.sender, "You cant confirm this");
        confirm_admin[id].status_admin = true;
        payable(msg.sender).transfer(transfers[confirm_admin[id].id_transfer].value/100*10);
    }
 
    function clime_transfer(uint id, uint code) public payable { 
        require(transfers[id].taker == msg.sender, "Not for you"); 
        require(transfers[id].status == false, "Transfer complite");
        require(code == transfers[id].code, "Wrong code");
        payable(msg.sender).transfer(transfers[id].value);
        transfers[id].status = true; 
    } 
 
    function chanle_transfer(uint id) public payable{ 
        require(transfers[id].giver == msg.sender, "You not gived it"); 
        require(transfers[id].status == false, "Transfer complite"); 
        payable(msg.sender).transfer(transfers[id].value);
        transfers[id].status = true;
    }

    function view_transactios_length() public view returns(uint) {
        return(transfers.length);
    }

    function create_shablon(string memory name) public {
        require(user_rule[msg.sender] == true);
        shablon_name[shablon_lenght] = name;
        shablon_lenght++;
    }

    function create_shablon_category(uint shablon_id, string memory catigory, uint value) public {
        require(user_rule[msg.sender] == true);
        require(shablon_id <= shablon_lenght);
        shablon_info[shablon_id].push(Shablon(catigory, value));
    }

    function create_vote() public {
        require(user_rule[msg.sender] == false, "You allready admin");
        address[] memory admins;
        votes.push(Vote(votes.length, msg.sender, admins, true));
    }
    
    function vote_yes(uint id) public {
        require(user_rule[msg.sender] == true, "Admins only");
        require(votes[id].status == true, "Vote complite");
        require(search_voter(id) == true, "You allready voted");
        votes[id].givers.push(msg.sender);
        if (votes[id].givers.length == admins.length) {
            votes[id].status = false;
            user_rule[votes[id].from] = true;
            admins.push(votes[id].from);
        }
    }

    function vote_no(uint id) public {
        require(user_rule[msg.sender] == true, "Admins only");
        require(votes[id].status == true, "Vote complite");
        require(search_voter(id) == true, "You allready voted");
        votes[id].givers.push(msg.sender);
        votes[id].status = false;
    }

    function search_voter(uint id) public view returns(bool) {
        for (uint i = 0; i < votes[id].givers.length; i++) {
            if (msg.sender == votes[id].givers[i]) {
                return(false);
            }
        }
        return(true);
    }

    function view_admins_length() public view returns(uint) {
        return(admins.length);
    }
    function view_shablons_length() public view returns(uint) {
        return(shablon_lenght);
    }
    function view_categores_length(uint id) public view returns(uint) {
        return(shablon_info[id].length);
    }
    function view_votes_length() public view returns(uint) {
        return(votes.length);
    }
    function view_confirm_admin_length() public view returns(uint) {
        return(confirm_admin.length);
    }
}