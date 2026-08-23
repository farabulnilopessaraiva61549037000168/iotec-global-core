;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="e57d73e5-d003-efbb-cfa9-9407f4575696")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,551904,e=>{"use strict";e.i(389959);var t=e.i(541793),s=e.i(814563),n=e.i(826771);e.i(473072);var r=e.i(489859),i=e.i(452317);let o=(0,s.createJSONStorage)(()=>({getItem:e=>r.default.get(e,"string"),setItem:(e,t)=>r.default.set(e,t),removeItem:e=>r.default.remove(e)})),a=(0,s.atomWithStorage)("areHiddenFilesVisible",!1,o),u=(0,t.atom)(null),l=(0,t.atom)((0,n.observableValue)(!1)),c=(0,t.atom)(!1),d=(0,t.atom)(void 0);(0,t.atom)([]);let p=(0,t.atom)(!1),S=(0,t.atom)(!1),m=(0,t.atom)(!1),f=(0,t.atom)(!1),T=(0,t.atom)(!1),h=(0,t.atom)(!1);e.s(["useAreHiddenFilesVisible",0,function(){return(0,i.useValue)(a)},"useCookieWarningBannerDismissed",0,function(){return(0,i.useValue)(c)},"useGetFileRenameInProgress",0,function(){return(0,i.useGet)(u)},"useGetHasCommitData",0,function(){return(0,i.useGet)(f)},"useHasCommitData",0,function(){return(0,i.useValue)(f)},"useInProgressMockupToAppGraduation",0,function(){return(0,i.useValue)(h)},"useIsFirstCheckpointCompleted",0,function(){return(0,i.useValue)(m)},"useIsPublishClickedCompleted",0,function(){return(0,i.useValue)(p)},"useSetAreHiddenFilesVisible",0,function(){return(0,i.useSet)(a)},"useSetCookieWarningBannerDismissed",0,function(){return(0,i.useSet)(c)},"useSetFileRenameInProgress",0,function(){return(0,i.useSet)(u)},"useSetHasCommitData",0,function(){return(0,i.useSet)(f)},"useSetInProgressMockupToAppGraduation",0,function(){return(0,i.useSet)(h)},"useSetIsFirstCheckpointCompleted",0,function(){return(0,i.useSet)(m)},"useSetIsFirstSessionCheckpointCompleted",0,function(){return(0,i.useSet)(T)},"useSetPublishClickedCompleted",0,function(){return(0,i.useSet)(p)},"useSetShouldShowRandomCheckpointSurvey",0,function(){return(0,i.useSet)(S)},"useShouldShowRandomCheckpointSurvey",0,function(){return(0,i.useValue)(S)},"useThreadFiltersPanelExpandedState",0,function(){return[(0,i.useValue)(d),(0,i.useSet)(d)]},"useWebviewPortOpenedObservable",0,function(){return(0,i.useValue)(l)}])},584888,e=>{"use strict";e.s(["convertTimestampToNumber",0,function(e){let{seconds:t,nanos:s}=e;return Number(t||0)+(s||0)/1e9},"getActiveFileForUser",0,function(e){for(let t of e.sessions.sort((e,t)=>e.timestamp-t.timestamp))if(t.activeFile)return t.activeFile;return null},"getUserForSession",0,function(e,t){let s=t.find(t=>t.sessions.some(t=>t.id===e));if(!s)throw Error(`Expected user with session ID ${e}`);return s}])},321164,e=>{"use strict";var t=e.i(973245),s=e.i(304277),n=e.i(566901),r=e.i(951262);let i={},o=t.gql`
    fragment WorkspaceSharedSecret on SharedSecret {
  id
  name
  description
  version
  timeCreated
  timeUpdated
  owner {
    __typename
    ... on User {
      id
    }
  }
  value
  signedUrl
}
    `,a=t.gql`
    fragment WorkspaceSharedSecretLink on SharedSecretLink {
  id
  alias
  secret {
    ...WorkspaceSharedSecret
  }
}
    ${o}`,u=t.gql`
    query SecretsPaneAuthorizations($replId: String!) {
  getRepl(id: $replId) {
    __typename
    ... on Repl {
      id
      isOwner
      authorizations {
        editSecrets {
          isAuthorized
          message
        }
      }
    }
    ... on Error {
      message
    }
  }
}
    `,l=t.gql`
    query WorkspaceSecrets($secretsInput: SecretsInput) {
  currentUser {
    id
    secrets(input: $secretsInput) {
      ... on SharedSecretConnection {
        items {
          ...WorkspaceSharedSecret
        }
        pageInfo {
          hasNextPage
          hasPreviousPage
          nextCursor
          previousCursor
        }
      }
    }
  }
}
    ${o}`,c=t.gql`
    query ReplLinkedSecrets($replId: String!) {
  getRepl(id: $replId) {
    __typename
    ... on Repl {
      id
      sharedSecretLinks {
        ...WorkspaceSharedSecretLink
      }
    }
  }
}
    ${a}`,d=t.gql`
    query WorkspaceAndReplLinkedSecrets($replId: String!) {
  currentUser {
    id
    secrets {
      ... on SharedSecretConnection {
        items {
          ...WorkspaceSharedSecret
        }
      }
    }
  }
  getRepl(id: $replId) {
    __typename
    ... on Repl {
      id
      sharedSecretLinks {
        ...WorkspaceSharedSecretLink
      }
    }
  }
}
    ${o}
${a}`,p=t.gql`
    mutation LinkSharedSecrets($input: LinkSharedSecretsInput!) {
  linkSharedSecrets(input: $input) {
    ... on LinkSharedSecretsResult {
      links {
        ...WorkspaceSharedSecretLink
      }
    }
    ... on Error {
      message
    }
  }
}
    ${a}`,S=t.gql`
    mutation UnlinkSharedSecrets($input: UnlinkSharedSecretsInput!) {
  unlinkSharedSecrets(input: $input) {
    ... on UnlinkSharedSecretsResult {
      success
    }
    ... on Error {
      message
    }
  }
}
    `,m=t.gql`
    mutation UpdateSharedSecretLink($input: UpdateSharedSecretLinkInput!) {
  updateSharedSecretLink(input: $input) {
    ... on UpdateSharedSecretLinkOutput {
      ...WorkspaceSharedSecretLink
    }
    ... on Error {
      message
    }
  }
}
    ${a}`;e.s(["ReplLinkedSecretsDocument",0,c,"WorkspaceSecretsDocument",0,l,"useLinkSharedSecretsMutation",0,function(e){let t={...i,...e};return r.useMutation(p,t)},"useReplLinkedSecretsQuery",0,function(e){let t={...i,...e};return s.useQuery(c,t)},"useSecretsPaneAuthorizationsQuery",0,function(e){let t={...i,...e};return s.useQuery(u,t)},"useUnlinkSharedSecretsMutation",0,function(e){let t={...i,...e};return r.useMutation(S,t)},"useUpdateSharedSecretLinkMutation",0,function(e){let t={...i,...e};return r.useMutation(m,t)},"useWorkspaceAndReplLinkedSecretsLazyQuery",0,function(e){let t={...i,...e};return n.useLazyQuery(d,t)},"useWorkspaceSecretsQuery",0,function(e){let t={...i,...e};return s.useQuery(l,t)}])},7106,e=>{"use strict";var t=e.i(276385),s=e.i(389959),n=e.i(541793),r=e.i(208008),i=e.i(594709),o=e.i(936423),a=e.i(933302);e.s(["DeploymentProvider",0,function(e){let u=(0,a.useExperimentParam)("autoscale_default_machine_config","default_vcpu","2"),l=(0,a.useExperimentParam)("autoscale_default_machine_config","default_memory","4"),[c]=(0,s.useState)(()=>(function({container:e,fs:t,dotReplit:s,ports:o,secrets:a,defaultMachineConfig:u}){let l=(0,n.createStore)();l.set(r.containerAtom,e),l.set(r.fsAtom,t),l.set(r.dotReplitAtom,s),l.set(r.portsAtom,o),l.set(r.secretsAtom,a);let c=i.CPUValues.findIndex(e=>e.toString()===u.vcpu),d=i.RAMValues.findIndex(e=>e.toString()===u.memory);return c>=0&&d>=0&&(l.set(i.cpuIndexAtom,c),l.set(i.ramIndexAtom,d)),l})({fs:e.fs,container:e.container,dotReplit:e.dotReplit,ports:e.ports,secrets:e.secrets,defaultMachineConfig:{vcpu:u,memory:l}}));return(0,t.jsxs)(o.DeploymentContext.Provider,{value:c,children:[e.children,(0,t.jsx)(r.Init,{replId:e.replId,orgId:e.orgId})]})}],7106)},463358,e=>{"use strict";var t=e.i(862927),s=e.i(973245);let n=s.gql`
    query GitAuth($input: GitProviderContextInput) {
  currentUser {
    id
    gitHubInfo {
      accessToken
    }
    gitHubInfoV2(input: $input) {
      accessToken
    }
    bitbucketInfo(input: $input) {
      accessToken
    }
  }
}
    `;var r=e.i(960933);let i=r.Type.Object({id:r.Type.String(),user_id:r.Type.Number(),ssh_hostname:r.Type.String(),token:r.Type.String()});var o=e.i(968323),a=e.i(423310),u=e.i(429843),l=e.i(871752);let c=["http:","https:","vscode:"];async function d({replId:e}){let s=await (0,o.tryCatchAsync)(()=>(0,l.postJson)(`/data/repls/${e}/get_ssh_token`));return s.error?{type:"error",message:s.error.toString()}:t.Value.Check(i,s.value)?{type:"success",data:s.value}:{type:"error",message:"Invalid JSON"}}async function p(e){if(!a.apolloClient)throw Error("Expected apollo");let{data:t}=await a.apolloClient.query({query:n,variables:{input:{orgId:e}}});if(!t?.currentUser)throw Error("Expected current user");return t.currentUser}function S(){document.activeElement instanceof HTMLElement&&document.activeElement.blur()}e.s(["default",0,function({container:e,fs:t,openMultipleFiles:s,openMultipleURLs:n,enableReplspaceSshTokenPassthrough:r=!1}){let i=new Set,o=!1,a=null;return e.openChannel({service:"open",name:"open"},({channel:e})=>{e.onCommand(e=>{if("replspaceApiOpenMultipleFiles"===e.body){if(!e.replspaceApiOpenMultipleFiles)throw Error("Expected replspaceApiOpenMultipleFiles");let{files:t,urls:r}=e.replspaceApiOpenMultipleFiles,i=r.flatMap(e=>{let t;try{t=new URL(e)}catch{return[]}return c.includes(t.protocol)?[t]:[]});s&&t.length>0&&(S(),s({paths:t})),n&&i.length>0&&(S(),n({urls:i.map(e=>e.toString())}))}})}),e.openChannel({service:"git",name:"git"},({channel:e})=>(e.onCommand(async n=>{switch(n.body){case"replspaceApiOpenFile":{if(!n.replspaceApiOpenFile)throw Error("Expected replspaceApiOpenFile");let{file:r,waitForClose:i,nonce:o}=n.replspaceApiOpenFile;if(s){if(S(),s({paths:[r]}),!i||!a)return;await a(r)}else{if(!r.endsWith(".git/COMMIT_EDITMSG")){i&&e.send({replspaceApiCloseFile:{file:r,nonce:o}}),window.alert(`tried to open ${r} but failed`);return}let s=window.prompt("Enter a commit message");if(await t.writeFile(r,s??""),!i)return}if(await t.flush(),"open"!==e.status)return;e.send({replspaceApiCloseFile:{file:r,nonce:o}});return}case"replspaceApiGetGitHubToken":{if(!n.replspaceApiGetGitHubToken)throw Error("Expected replspaceApiGetGitHubToken");let t=()=>{"open"===e.status&&e.send({replspaceApiGitHubToken:{token:"",nonce:n.replspaceApiGetGitHubToken?.nonce}})},s=await p();if(null==s.gitHubInfoV2&&null==s.gitHubInfo)return void t();if(!i.size){t(),u.logger.error("Got a replspaceApiGetGitHubToken command but no confirm listener is set up");return}let r=()=>{"open"===e.status&&e.send({replspaceApiGitHubToken:{token:s.gitHubInfoV2?.accessToken??s.gitHubInfo?.accessToken,nonce:n.replspaceApiGetGitHubToken?.nonce}})};if(o)return void r();let a=!1,l=()=>{for(let e of i)e(null)};for(let e of i){if(a)break;e((e,s=!0)=>{if(!a){if(a=!0,!e){t(),l();return}s&&(o=e),r(),l()}})}return}case"replspaceApiGetBitbucketToken":{if(!n.replspaceApiGetBitbucketToken)throw Error("Expected replspaceApiGetBitbucketToken");let t=()=>{"open"===e.status&&e.send({replspaceApiBitbucketToken:{token:"",nonce:n.replspaceApiGetBitbucketToken?.nonce}})},s=await p();if(null==s.bitbucketInfo)return void t();if(!i.size){t(),u.logger.error("Got a replspaceApiGetBitbucketToken command but no confirm listener is set up");return}let r=()=>{"open"===e.status&&e.send({replspaceApiBitbucketToken:{token:s.bitbucketInfo?.accessToken,nonce:n.replspaceApiGetBitbucketToken?.nonce}})};if(o)return void r();let a=!1,l=()=>{for(let e of i)e(null)};for(let e of i){if(a)break;e((e,s=!0)=>{if(!a){if(a=!0,!e){t(),l();return}s&&(o=e),r(),l()}})}}}}),()=>{})),r&&e.openChannel({service:"sshtoken",name:"sshtoken"},({channel:e})=>{e.onCommand(async t=>{if(!t.replspaceApiSSHTokenGetRequest)throw Error("Expected replspaceApiSSHTokenGetRequest");let{nonce:s,replid:n}=t.replspaceApiSSHTokenGetRequest,r=t=>{"open"===e.status&&e.send({replspaceApiSSHTokenGetResponse:t})},i=await d({replId:n});if("open"===e.status){if("error"===i.type){r({token:"",nonce:s}),u.logger.error(i.message);return}r({token:i.data.token,nonce:s,sshHostname:i.data.ssh_hostname})}})}),{onConfirmSendToken(e){let t=t=>e(t);return i.add(t),()=>{i.delete(t)}},setWaitForFileClose:function(e){a=e}}},"fetchReplSshToken",0,d],463358)},949955,e=>{"use strict";var t,s=e.i(866408),n=e.i(205104),r=e.i(127387),i=((t={}).USER_JOIN="USER_JOIN",t.USER_LEAVE="USER_LEAVE",t.USERS_UPDATE="USERS_UPDATE",t.USER_OPENED_FILE="USER_OPENED_FILE",t),o=e.i(584888),a=e.i(383941);e.s(["default",0,function({container:e,onCommand:t}){let u=(0,s.default)();u.setMaxListeners(1/0);let l=[],c={},d=null;async function p(){return d||new Promise(e=>{u.once(i.USERS_UPDATE,()=>{if(!d)throw Error("Expected presenceChannel to be set");e(d)})})}return e.openChannel({service:"presence",name:"presencer"},({channel:e})=>(e.onCommand(e=>{t?.(e);let s={cmd:e,emitter:u,activeUsers:l,userIdToFile:c};switch(e.body){case"roster":!function({cmd:e,emitter:t,activeUsers:s,userIdToFile:n}){let r=e.roster;if(!r)return;let{user:u,files:l}=r;if(!u||!l)return;let c=new Set;s.splice(0,s.length),u.forEach(e=>{if(!e.id||!e.name||!e.roles||c.has(e.id))return;let t=l.filter(t=>t.userId===e.id).map(e=>{if(!e.session||!e.timestamp)throw Error("Expected session and associated with user");return{id:e.session,activeFile:e.file||null,timestamp:(0,o.convertTimestampToNumber)(e.timestamp)}});s.push({id:e.id,username:e.name,roles:e.roles,color:(0,a.getColorForName)(e.name),sessions:t}),c.add(e.id)}),s.forEach(e=>{n[e.id]=(0,o.getActiveFileForUser)(e)}),t.emit(i.USERS_UPDATE,[...s])}(s);break;case"join":!function({cmd:e,emitter:t,activeUsers:s,userIdToFile:n}){let u=e.join;if(!u.id||!u.name||!u.roles||!u.session)return;let l=s.find(e=>e.id===u.id),c=Math.floor(Date.now()/1e3),d=r.google.protobuf.Timestamp.create({seconds:c}),p=(0,o.convertTimestampToNumber)(d);if(l)l.sessions.some(e=>e.id===u.session)||l.sessions.push({id:u.session,activeFile:null,timestamp:p});else{let e={id:u.id,username:u.name,roles:u.roles,color:(0,a.getColorForName)(u.name),sessions:[{id:u.session,activeFile:null,timestamp:p}]};n[u.id]=null,s.push(e),t.emit(i.USER_JOIN,e),t.emit(i.USERS_UPDATE,[...s])}}(s);break;case"part":!function({cmd:e,emitter:t,activeUsers:s,userIdToFile:n}){if(!e.part||!e.part.id||!e.part.session)return;let{id:r,session:a}=e.part,u=s.findIndex(e=>e.id===r),l=s[u];if(1===l.sessions.length)s.splice(u,1),delete n[l.id],t.emit(i.USER_LEAVE,l),t.emit(i.USERS_UPDATE,[...s]);else{l.sessions=l.sessions.filter(e=>e.id!==a);let e=(0,o.getActiveFileForUser)(l);n[l.id]!==e&&(n[l.id]=e,t.emit(i.USER_OPENED_FILE,{user:l,file:e}))}}(s);break;case"fileOpened":!function({emitter:e,cmd:t,activeUsers:s,userIdToFile:n}){if(!t.fileOpened)return;let{userId:r,file:a,timestamp:u,session:l}=t.fileOpened,c=a||null;if(!r||!u)throw Error("Expected userId and timestamp associated with file opened command");let d=s.find(e=>e.id===r);if(!d)throw Error(`Expected user with ID ${r}`);let p=d.sessions.find(e=>e.id===l);if(!p)throw Error(`Expected session with ID ${p}`);p.activeFile=c,p.timestamp=(0,o.convertTimestampToNumber)(u),n[r]=c,e.emit(i.USER_OPENED_FILE,{user:d,file:c})}(s);break;case"sessionTimestampUpdated":!function({cmd:e,emitter:t,activeUsers:s,userIdToFile:n}){let r=e.sessionTimestampUpdated;if(!r.session||!r.timestamp)throw Error("Expected session and tiemstamp associated with update");let a=r.session,u=(0,o.getUserForSession)(a,s),l=n[u.id],c=u.sessions.find(e=>e.id===a);if(!c)throw Error(`Expected user ${u.id} to have a session with ID ${a}`);c.timestamp=(0,o.convertTimestampToNumber)(r.timestamp);let{activeFile:d}=c;d!==l&&(n[u.id]=d,t.emit(i.USER_OPENED_FILE,{user:u,file:d}))}(s)}}),d=e,()=>{d=null})),{onUserLeave:e=>(u.on(i.USER_LEAVE,e),()=>{u.removeListener(i.USER_LEAVE,e)}),onUserJoin:e=>(u.on(i.USER_JOIN,e),()=>{u.removeListener(i.USER_JOIN,e)}),onActiveUsersChange:e=>(u.on(i.USERS_UPDATE,e),()=>{u.removeListener(i.USERS_UPDATE,e)}),onUserOpenedFile:e=>(u.on(i.USER_OPENED_FILE,e),()=>{u.removeListener(i.USER_OPENED_FILE,e)}),getActiveFileForUser(e){let t=c[e];if(void 0===t)throw Error(`Expected file for user with ID ${e} to be defined`);return t},async updateOpenFile(e){(await p()).send({openFile:{file:e}})},async updateSessionTimestamp(){(await p()).send({updateSessionTimestamp:{}})},getActiveUsers:()=>l,getUserIdToFile:()=>c,getPathToUserIds(){let e=new Map;return l.forEach(({id:t})=>{let s=c[t];s&&function t(s,r){if(""===s)return;e.has(s)||e.set(s,[]);let i=e.get(s);if(!i)throw Error("Expected user Ids");i.some(e=>e===r)||(e.get(s)?.push(r),t((0,n.getParentPath)(s),r))}(s,t)}),e}}}],949955)},82775,e=>{"use strict";var t=e.i(389959),s=e.i(231693),n=e.i(464458),r=e.i(19004),i=e.i(635431),o=e.i(17609),a=e.i(748855),u=e.i(415541),l=e.i(101597),c=e.i(563654),d=e.i(478074),p=e.i(30083),S=e.i(540082),m=e.i(949955),f=e.i(463358),T=e.i(70);function h({onUnrecoverableError:e,openMultipleFiles:t,openMultipleURLs:s,enableReplspaceSshTokenPassthrough:n,onPresenceCommand:k,replId:g,ctx:E}){let _=(0,l.default)({onUnrecoverableError:e,ctx:E}),v=(0,c.default)({container:_}),I=(0,m.default)({container:_,onCommand:k}),A=(0,r.default)({container:_,fs:v,ctx:E}),x=(0,i.default)({container:_}),w=(0,a.default)({container:_,dotReplit:A}),C=(0,o.default)({container:_,track:u.track}),b=(0,f.default)({container:_,fs:v,openMultipleFiles:t,openMultipleURLs:s,enableReplspaceSshTokenPassthrough:n}),U=(0,S.createPortsService)({container:_,dotReplit:A}),y=(0,p.createLSPNixService)({container:_,toolchain:w,fs:v}),L=(0,d.default)({container:_,fs:v,replId:g}),R=(0,T.default)({container:_});return{presence:I,packager:C,container:_,fs:v,dotReplit:A,nixService:x,lspnix:y,git:L,replspaceApi:b,toolchain:w,ports:U,secrets:R}}e.s(["default",0,h,"useCreateServices",0,function(e){let[r,i]=(0,t.useState)(null);return(0,t.useEffect)(()=>{let t=(0,n.createSpanFromContext)(s.context.active(),"workspace.useCreateServices"),r=h({...e,ctx:t?.childCtx});return t?.span.end(),i(r),()=>{i(null),setTimeout(()=>{r.container.destroy()},500)}},[e]),r}])},462985,e=>{"use strict";var t=e.i(973245),s=e.i(304277);e.i(566901);let n={},r=t.gql`
    query CheckpointReplHideUsageCost($replId: String!) {
  getRepl(id: $replId) {
    __typename
    ... on Repl {
      id
      authorizations {
        hideUsageCost {
          isAuthorized
        }
      }
    }
  }
}
    `;var i=e.i(473072);e.s(["useHideUsageCost",0,function(){var e;let t,{data:o,loading:a}=(e={variables:{replId:(0,i.default)()}},t={...n,...e},s.useQuery(r,t));return!!a||o?.getRepl?.__typename==="Repl"&&(o.getRepl.authorizations?.hideUsageCost?.isAuthorized??!1)}],462985)},979071,e=>{"use strict";e.i(925218);var t=e.i(641555);let s={direction:"reverse",state:{id:null,event:null,state:null,senderType:null},reducer:(e,t)=>(t.id=e.id,t.state=e.state,t.event=e,t.senderType=e.sender.type,!1)};e.s(["useLastEvent",0,function(e){return(0,t.useObservableMemo)(()=>e?.reduce(s,1),[e],{default:null})}])},632732,e=>{"use strict";var t=e.i(82259);let s=[t.TaskStatus.TASK_STATUS_PENDING,t.TaskStatus.TASK_STATUS_IN_PROGRESS];e.s(["getCompletedTasks",0,function({tasks:e}){return e.filter(e=>e.updated).filter(e=>e.status===t.TaskStatus.TASK_STATUS_COMPLETED)},"getTaskSummary",0,function(e){return e.summary&&""!==e.summary?e.summary:e.content},"isFirstInstanceOfTaskList",0,function({tasks:e}){return!!e&&0!==e.length&&e.every(e=>e.updated&&s.includes(e.status))},"isFullyCompletedTaskList",0,function(e){return e.length>0&&e.every(e=>e.status===t.TaskStatus.TASK_STATUS_COMPLETED)},"isPlanModeProposedTaskList",0,function(e){return e.agentMode===t.AgentMode.AGENT_MODE_DISCUSSION}])},617603,e=>{e.v({button:"TaskListCost-module__6lzpnq__button",loadingPlaceholder:"TaskListCost-module__6lzpnq__loadingPlaceholder","skeleton-data-loading":"TaskListCost-module__6lzpnq__skeleton-data-loading"})},614888,90057,e=>{"use strict";var t=e.i(276385),s=e.i(389959),n=e.i(76112),r=e.i(110232),i=e.i(488299),o=e.i(8047),a=e.i(244945),u=e.i(61732),l=e.i(617603);e.s(["TaskListCost",0,function({cents:e,isExpanded:c,setIsExpanded:d}){let p=(0,s.useCallback)(()=>{d(!c),c||(0,r.trackAgentAnalyticsEvent)({action:"viewed_task_list_usage_cost"})},[c,d]);return(0,t.jsxs)(u.View,{row:!0,align:"center",gap:8,children:[(0,t.jsx)(i.IconButton,{alt:"Agent Usage",onClick:p,clsx:l.default.button,children:(0,t.jsx)(n.default,{})}),c?null==e?(0,t.jsx)(a.Tooltip,{tooltip:"Loading usage information…",children:(0,t.jsx)(u.View,{clsx:l.default.loadingPlaceholder})}):(0,t.jsxs)(o.Text,{color:"dimmer",variant:"small",children:["$",(e/100).toFixed(2)]}):null]})}],614888);var c=e.i(374106);e.i(668201);var d=e.i(15442);e.i(925218);var p=e.i(587467),S=e.i(641555);let m={direction:"reverse",state:{event:void 0},debug:{name:"LastEndOfRunSummaryEventOrSessionCreationReducer"},reducer(e,t){if((0,c.isEventAgentToolDataKind)(e,"endOfRunSummaryData")||(0,c.isEventContentsKind)(e,"sessionCreationEventContents"))return t.event=e,!1}};e.s(["useAgentUsageSinceLastBillingEvent",0,function(e){let t=(0,d.useChatter)(),s=(0,p.useObservable)(t.sessions.agent.current),n=(0,S.useObservableMemo)(()=>s?.reduce(m,"global"),[s],{default:void 0}),r=n?.event?.created;return(0,S.useObservableMemo)(()=>e&&r?s?.agent.usage(r):void 0,[s,r,e])}],90057)},38885,e=>{"use strict";var t=e.i(374106);e.i(668201);var s=e.i(15442);e.i(925218);var n=e.i(587467),r=e.i(979071);e.s(["useIsAgentUsageShownInLatestEvent",0,function(){let e=(0,s.useChatter)(),i=(0,n.useObservable)(e.sessions.agent.current),o=(0,r.useLastEvent)(i);return!!o?.event&&(0,t.isEventAgentToolDataKind)(o.event,"endOfRunSummaryData")}])},615965,e=>{e.v({rotate:"TaskStatusIcon-module__WYKDlW__rotate",rotatingIcon:"TaskStatusIcon-module__WYKDlW__rotatingIcon"})},574966,e=>{e.v({chevronIconContainer:"TaskListDrawer-module__f-SkTa__chevronIconContainer",drawerItems:"TaskListDrawer-module__f-SkTa__drawerItems",drawerSurface:"TaskListDrawer-module__f-SkTa__drawerSurface",emptyIconContainer:"TaskListDrawer-module__f-SkTa__emptyIconContainer",showMoreButton:"TaskListDrawer-module__f-SkTa__showMoreButton",statusIconContainer:"TaskListDrawer-module__f-SkTa__statusIconContainer",taskContent:"TaskListDrawer-module__f-SkTa__taskContent",truncatedSection:"TaskListDrawer-module__f-SkTa__truncatedSection"})},224071,288219,e=>{"use strict";var t=e.i(276385),s=e.i(389959),n=e.i(82259),r=e.i(167392),i=e.i(568430),o=e.i(614888),a=e.i(90057),u=e.i(38885),l=e.i(462985),c=e.i(632732),d=e.i(183035),p=e.i(851722),S=e.i(806685),m=e.i(429662),f=e.i(62342),T=e.i(753451),h=e.i(480028),k=e.i(244945),g=e.i(61732),E=e.i(615965);function _({status:e,oldStatus:s,tooltipContent:r,color:i}){let o=(0,T.useIsInMobileWorkspace)(),a=i??h.tokens.foregroundDimmer,u=i??h.tokens.foregroundDimmest;switch(e){case n.TaskStatus.TASK_STATUS_COMPLETED:if(s===n.TaskStatus.TASK_STATUS_COMPLETED_PENDING_REVIEW)return(0,t.jsx)(k.Tooltip,{tooltip:r??"Task completed & reviewed",isDisabled:o,children:(0,t.jsx)(f.default,{color:a,size:16})});return(0,t.jsx)(k.Tooltip,{tooltip:r??"Task completed",isDisabled:o,children:(0,t.jsx)(d.default,{color:a,size:16})});case n.TaskStatus.TASK_STATUS_IN_PROGRESS:return(0,t.jsx)(k.Tooltip,{tooltip:r??"Task in progress",isDisabled:o,children:(0,t.jsx)(g.View,{clsx:E.default.rotatingIcon,align:"center",justify:"center",children:(0,t.jsx)(S.default,{color:a,size:16})})});case n.TaskStatus.TASK_STATUS_COMPLETED_PENDING_REVIEW:return(0,t.jsx)(k.Tooltip,{tooltip:r??"Task completed, pending review",isDisabled:o,children:(0,t.jsx)(m.default,{color:a,size:16})});case n.TaskStatus.TASK_STATUS_PENDING:default:return(0,t.jsx)(k.Tooltip,{tooltip:r??"Task pending",isDisabled:o,children:(0,t.jsx)(p.default,{color:u,size:16})})}}e.s(["TaskStatusIcon",0,_],288219);var v=e.i(406664),I=e.i(919073),A=e.i(66742),x=e.i(8047),w=e.i(574966);function C({task:e,approvalStatus:s}){let r="proposed"!==s;return(0,t.jsxs)(g.View,{clsx:w.default.taskItem,row:!0,justify:"space-between",align:"center",gap:8,px:8,py:4,children:[(0,t.jsx)(g.View,{grow:!0,shrink:!0,children:(0,t.jsx)(x.Text,{clsx:w.default.taskContent,color:function(e,t){return"proposed"===t?"default":e===n.TaskStatus.TASK_STATUS_COMPLETED||e===n.TaskStatus.TASK_STATUS_COMPLETED_PENDING_REVIEW?"dimmest":e===n.TaskStatus.TASK_STATUS_PENDING?"dimmer":"default"}(e.status,s),children:(0,c.getTaskSummary)(e)})}),r?(0,t.jsx)(g.View,{clsx:w.default.statusIconContainer,p:4,align:"center",justify:"center",children:(0,t.jsx)(_,{...e})}):null]})}function b({tasks:e,approvalStatus:s}){return(0,t.jsx)(t.Fragment,{children:e.map(e=>(0,t.jsx)(C,{task:e,approvalStatus:s},e.id))})}function U({innerRef:e,approvalStatus:a,placement:u,isCollapsed:l,setIsCollapsed:d,agentUsage:p,isCostInfoExpanded:S,setIsCostInfoExpanded:m,isCostInfoHidden:f=!1,...T}){let h=u??("proposed"===a?"bottom":"top"),{tasks:E}=T,[C,y]=(0,s.useState)(!1),L=(0,s.useRef)(null),R=E.filter(e=>e.status===n.TaskStatus.TASK_STATUS_COMPLETED||e.status===n.TaskStatus.TASK_STATUS_COMPLETED_PENDING_REVIEW).length,D=(0,c.isFullyCompletedTaskList)(E),P=(0,s.useMemo)(()=>{let e=[],t=[],s=[],r=[];return E.forEach(i=>{switch(i.status){case n.TaskStatus.TASK_STATUS_COMPLETED:e.push(i);break;case n.TaskStatus.TASK_STATUS_COMPLETED_PENDING_REVIEW:r.push(i);break;case n.TaskStatus.TASK_STATUS_IN_PROGRESS:t.push(i);break;case n.TaskStatus.TASK_STATUS_PENDING:default:s.push(i)}}),{completed:e,completedPendingReview:r,inProgress:t,pending:s}},[E]),O=!D&&P.completed.length>3,j=O&&!C?P.completed.length-3:0,F=O&&!C?P.completed.slice(j):P.completed,N=(0,s.useMemo)(()=>P.inProgress[0],[P.inProgress]),G=(0,s.useMemo)(()=>"proposed"===a?"Planned tasks":D?"Completed tasks":l&&N?(0,c.getTaskSummary)(N):"In progress tasks",[a,l,N,D]),M=(0,v.useCreateInteractive)({variant:"nofill",borderRadius:0});return(0,t.jsxs)(I.ShadesSurface,{clsx:w.default.drawerSurface,gap:4,grow:1,shrink:1,innerRef:e,elevate:"approved"===a&&"2x",children:[(0,t.jsxs)(I.ShadesSurface,{clsx:M.clsx,style:M.style,elevate:!1,border:l?void 0:{side:"bottom",strength:"subtle"},row:!0,gap:4,align:"center",justify:"space-between",py:8,pl:4,pr:12,onClick:()=>d(e=>!e),children:[(0,t.jsxs)(g.View,{row:!0,gap:8,align:"center",shrink:!0,children:[(0,t.jsx)(k.Tooltip,{tooltip:l?"Expand":"Collapse",children:(0,t.jsx)(g.View,{clsx:w.default.chevronIconContainer,align:"center",justify:"center",children:"bottom"===h?l?(0,t.jsx)(i.default,{}):(0,t.jsx)(r.default,{}):l?(0,t.jsx)(r.default,{}):(0,t.jsx)(i.default,{})})}),(0,t.jsx)(x.Text,{color:"dimmer",ref:L,shrink:!0,multiline:!1,showTooltipOnTruncate:!0,children:G})]}),"proposed"!==a?(0,t.jsxs)(g.View,{row:!0,gap:8,align:"center",children:[(0,t.jsxs)(x.Text,{color:"dimmer",variant:"small",children:[R," / ",E.length]}),N&&l?(0,t.jsx)(g.View,{pr:2,children:(0,t.jsx)(_,{...N})}):null,f||l?null:(0,t.jsx)(o.TaskListCost,{cents:p?.cents,isExpanded:S,setIsExpanded:m})]}):null]}),l?null:(0,t.jsxs)(g.View,{clsx:w.default.drawerItems,shrink:!0,px:2,pb:8,children:[O&&!C?(0,t.jsx)(g.View,{clsx:w.default.truncatedSection,children:(0,t.jsx)(g.View,{row:!0,justify:"center",align:"center",p:2,children:(0,t.jsx)(A.PillButton,{clsx:w.default.showMoreButton,onClick:()=>y(!0),text:`Show ${j} more completed task${1===j?"":"s"}`})})}):null,(0,t.jsx)(b,{tasks:[...F,...P.completedPendingReview,...P.inProgress,...P.pending],approvalStatus:a}),0===E.length?(0,t.jsxs)(g.View,{row:!0,px:2,align:"center",gap:4,children:[(0,t.jsx)(g.View,{clsx:w.default.emptyIconContainer}),(0,t.jsx)(x.Text,{color:"dimmest",children:"No tasks to show"})]}):null]})]})}e.s(["TaskListDrawer",0,function({approvalStatus:e,...n}){let[r,i]=(0,s.useState)(("approved"===e)??"approved"===e),[o,c]=(0,s.useState)(!1),d=(0,l.useHideUsageCost)(),p=(0,u.useIsAgentUsageShownInLatestEvent)(),S=(0,a.useAgentUsageSinceLastBillingEvent)(!p&&!d&&o);return(0,t.jsx)(U,{...n,approvalStatus:e,isCollapsed:r,setIsCollapsed:i,isCostInfoExpanded:o,setIsCostInfoExpanded:c,agentUsage:S,isCostInfoHidden:p||d})},"TaskListDrawerUI",0,U,"TaskListItems",0,b],224071)}]);

//# debugId=e57d73e5-d003-efbb-cfa9-9407f4575696
//# sourceMappingURL=109c9nujgv6qz.js.map
