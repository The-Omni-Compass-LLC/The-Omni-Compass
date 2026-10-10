// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// All patents, copyrights and trademarks filed in the USA. Evaluation and simulation use only; any commercialization,
// monetization or other use requires a signed, paid Omni-Compass Enterprise License. Subject to change at any time;
// www.omni-compass.com is the authority of record. See LICENSE, NOTICE and DISCLOSURES.md.
#include "omnicompass/core.hpp"
#include <iostream>
int main(int argc,char**argv){if(argc!=3){std::cerr<<"usage: oc_run_fixture INPUT.csv OUTPUT.csv\n";return 2;}try{auto in=omnicompass::read_inputs(argv[1]);std::vector<omnicompass::Result>out;out.reserve(in.size());for(auto&x:in)out.push_back(omnicompass::simulate(x));omnicompass::write_results(argv[2],out);std::cout<<"processed "<<out.size()<<" current-engine fixtures\n";return 0;}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
