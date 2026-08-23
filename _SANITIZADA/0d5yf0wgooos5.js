;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="e4c27179-9ebb-2c72-40d7-e6d5d12c4d57")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,546180,e=>{"use strict";var t=e.i(973245),r=e.i(319801),l=e.i(517414);let a=t.gql`
    fragment ReplCardArtifact on ReplArtifact {
  artifactId
  title
  kind
  previewPath
  latestScreenshotUri
}
    `;var i=e.i(272290);let n=t.gql`
    fragment ShadesReplCardRepl on Repl {
  id
  title
  iconUrl
  isPrivate
  isStarred
  isCurrentUserStarred
  timeUpdated
  lastOpened
  latestAgentScreenshotUrl
  ...ReplLinkRepl
  ...ComponentsReplActions
  artifacts {
    ...ReplCardArtifact
  }
  user {
    id
    username
    fullName
    image
  }
  hostingDeployment {
    __typename
    ... on HostingDeployment {
      id
      ...DeploymentItem
      latestBuildStatus
      currentBuild {
        id
        status
        timeCreated
        artifacts {
          ...HostingBuildArtifactFields
        }
        user {
          id
          displayName
        }
      }
    }
  }
  authorizations {
    star {
      isAuthorized
    }
    viewFileContents {
      isAuthorized
      code
      message
    }
    editFileContents {
      isAuthorized
      code
      message
    }
  }
}
    ${r.ReplLinkReplFragmentDoc}
${l.ComponentsReplActionsFragmentDoc}
${a}
${i.DeploymentItemFragmentDoc}
${i.HostingBuildArtifactFieldsFragmentDoc}`;e.s(["ShadesReplCardReplFragmentDoc",0,n],546180)},193207,e=>{e.v({popover:"SearchableSelect-module__mRLXPq__popover"})},658904,e=>{"use strict";var t=e.i(276385),r=e.i(389959),l=e.i(255615),a=e.i(585544),i=e.i(773222),n=e.i(404488),s=e.i(877009),o=e.i(193207);e.s(["SearchableSelect",0,function({trigger:e,onInputChange:d,inputValue:u,maxHeight:p,headerContent:c,...m}){let[y,h]=(0,r.useState)(!1),g=(0,r.useCallback)(e=>{("ArrowDown"===e.key||"ArrowUp"===e.key)&&h(!0)},[]);return(0,t.jsxs)(i.PopoverTrigger,{isOpen:y,onOpenChange:h,label:"Select",placement:"bottom start",clsx:o.default.popover,maxHeight:p,children:[({onClick:r,...a})=>(0,t.jsx)(l.ButtonContext.Provider,{value:{...a,onPress:r,onKeyDown:g},children:e}),(0,t.jsxs)(n.SearchableListBox,{children:[c,(0,t.jsx)(s.SearchField,{autoFocus:!c,onChange:d,value:u}),(0,t.jsx)(a.ListBox,{...m,children:m.children})]})]})}])},597039,e=>{"use strict";var t=e.i(973245),r=e.i(180273),l=e.i(304277);e.i(566901);let a={},i=t.gql`
    query IsUnifiedPlanEnabledPersonal {
  currentUser {
    ...IsUnifiedPlanEnabledPersonalWorkspaceCurrentUser
  }
}
    ${r.IsUnifiedPlanEnabledPersonalWorkspaceCurrentUserFragmentDoc}`;var n=e.i(856010);e.s(["useIsUnifiedPlanEnabledPersonal",0,function(e){var t;let r,{data:s,loading:o}=(t={skip:e?.skip},r={...a,...t},l.useQuery(i,r)),d=s?.currentUser?.__typename==="CurrentUser"?s.currentUser:void 0;return{isUnifiedPlanEnabled:(0,n.useIsUnifiedPlanEnabled)({currentUser:d}),loading:o}}],597039)},99170,e=>{e.v({folderActions:"ManageFoldersModal-module__1M5cGa__folderActions",folderItem:"ManageFoldersModal-module__1M5cGa__folderItem",folderList:"ManageFoldersModal-module__1M5cGa__folderList",folderName:"ManageFoldersModal-module__1M5cGa__folderName",folderRow:"ManageFoldersModal-module__1M5cGa__folderRow"})},189603,e=>{e.v({accessFilterButton:"ReplsFilters-module__NahJ0a__accessFilterButton",buildTypeFilterButton:"ReplsFilters-module__NahJ0a__buildTypeFilterButton",creatorFilterButton:"ReplsFilters-module__NahJ0a__creatorFilterButton",creatorFilterItem:"ReplsFilters-module__NahJ0a__creatorFilterItem",creatorItemContent:"ReplsFilters-module__NahJ0a__creatorItemContent",creatorList:"ReplsFilters-module__NahJ0a__creatorList",creatorMeSurface:"ReplsFilters-module__NahJ0a__creatorMeSurface",folderFilterButton:"ReplsFilters-module__NahJ0a__folderFilterButton",statusFilterButton:"ReplsFilters-module__NahJ0a__statusFilterButton"})},802684,e=>{e.v({cardSkeleton:"ReplsGrid-module__TXZKiW__cardSkeleton",grid:"ReplsGrid-module__TXZKiW__grid",pulse:"ReplsGrid-module__TXZKiW__pulse"})},710596,e=>{e.v({table:"ReplsTable-module__ghmu1q__table",tableWrapper:"ReplsTable-module__ghmu1q__tableWrapper",titleCell:"ReplsTable-module__ghmu1q__titleCell",titleText:"ReplsTable-module__ghmu1q__titleText",wrapper:"ReplsTable-module__ghmu1q__wrapper"})},117964,e=>{e.v({container:"ReplsView-module__4M54Uq__container",filterBar:"ReplsView-module__4M54Uq__filterBar",searchBarWrapper:"ReplsView-module__4M54Uq__searchBarWrapper",viewSwitcher:"ReplsView-module__4M54Uq__viewSwitcher"})},921851,56268,e=>{"use strict";var t=e.i(730497),r=e.i(410345),l=e.i(597039);e.s(["useIsAppManagementEnabled",0,function({orgSlug:e}){let a=!!e,i=(0,t.useFlag)({controlName:"flag-app-management"}),{isUnifiedPlanEnabled:n,loading:s}=(0,r.useIsUnifiedPlanEnabledOrgSlug)(e??"",{skip:i||!a}),{isUnifiedPlanEnabled:o,loading:d}=(0,l.useIsUnifiedPlanEnabledPersonal)({skip:i||a}),u=a?n:o,p=a?s:d;return{shouldShowAppPageV2:u||i,loading:!i&&p}}],921851);var a=e.i(276385),i=e.i(488081),n=e.i(389959),s=e.i(960933),o=e.i(862927);let d=s.Type.Object({domains:s.Type.Optional(s.Type.Array(s.Type.String())),id:s.Type.Optional(s.Type.String({description:"A stable identifier for the artifact that persists across folder renames. When absent, the folder name is used as the artifact identity."})),integratedSkills:s.Type.Optional(s.Type.Array(s.Type.Object({name:s.Type.Optional(s.Type.String()),version:s.Type.Optional(s.Type.String())}))),kind:s.Type.Optional(s.Type.Union([s.Type.Literal("web"),s.Type.Literal("slides"),s.Type.Literal("video"),s.Type.Literal("mobile"),s.Type.Literal("automation"),s.Type.Literal("game"),s.Type.Literal("data-app"),s.Type.Literal("cli"),s.Type.Literal("vnc"),s.Type.Literal("api"),s.Type.Literal("design"),s.Type.Literal("custom")])),pageMetadata:s.Type.Optional(s.Type.Array(s.Type.Object({path:s.Type.String(),screenshotTimestamp:s.Type.Optional(s.Type.String()),screenshotUri:s.Type.Optional(s.Type.String())}))),previewDomain:s.Type.Optional(s.Type.String()),previewPath:s.Type.Optional(s.Type.String()),previewPort:s.Type.Optional(s.Type.Number({description:"The port that the workspace preview connects to. Only valid when router is port."})),router:s.Type.Optional(s.Type.Union([s.Type.Literal("port"),s.Type.Literal("path"),s.Type.Literal("domain"),s.Type.Literal("expo-domain")],{description:"The preview routing strategy. port (legacy), path, domain, or expo-domain."})),services:s.Type.Optional(s.Type.Array(s.Type.Object({development:s.Type.Object({run:s.Type.Union([s.Type.Object({args:s.Type.Array(s.Type.String()),env:s.Type.Optional(s.Type.Record(s.Type.String(),s.Type.String()))},{additionalProperties:!1}),s.Type.String(),s.Type.Array(s.Type.String())],{description:"The command to run the service during development."})},{description:"Configuration for running the service during development."}),ensurePreviewReachable:s.Type.Optional(s.Type.String({description:"Path to ensure is reachable before showing the preview."})),env:s.Type.Optional(s.Type.Record(s.Type.String(),s.Type.String())),localPort:s.Type.Number({description:"The port the service listens on."}),name:s.Type.String({description:"The service name, which becomes the workflow name for development."}),paths:s.Type.Optional(s.Type.Array(s.Type.String(),{description:"Path prefixes that will be routed to this service."})),production:s.Type.Optional(s.Type.Object({build:s.Type.Optional(s.Type.Union([s.Type.Object({args:s.Type.Array(s.Type.String()),env:s.Type.Optional(s.Type.Record(s.Type.String(),s.Type.String()))},{additionalProperties:!1}),s.Type.String(),s.Type.Array(s.Type.String())],{description:"Command to build the project for production."})),health:s.Type.Optional(s.Type.Object({liveness:s.Type.Optional(s.Type.Object({headers:s.Type.Optional(s.Type.Record(s.Type.String(),s.Type.String())),path:s.Type.Optional(s.Type.String({description:"The path for the check. For example, `/ready`. Defaults to `/`."}))})),startup:s.Type.Optional(s.Type.Object({headers:s.Type.Optional(s.Type.Record(s.Type.String(),s.Type.String())),path:s.Type.Optional(s.Type.String({description:"The path for the check. For example, `/ready`. Defaults to `/`."}))}))},{description:"Configuration for production healthchecks."})),publicDir:s.Type.Optional(s.Type.String({description:"Root directory for static file serving. Only valid when serve is 'static'."})),responseHeaders:s.Type.Optional(s.Type.Array(s.Type.Object({name:s.Type.Optional(s.Type.String({description:"The name of the header to add."})),path:s.Type.Optional(s.Type.String({description:"The pattern to apply the header to."})),value:s.Type.Optional(s.Type.String({description:"The value of the header to add."}))}),{description:"Headers to apply to responses for static serving. Only valid when serve is 'static'."})),rewrites:s.Type.Optional(s.Type.Array(s.Type.Object({from:s.Type.Optional(s.Type.String({description:"The pattern to rewrite."})),to:s.Type.Optional(s.Type.String({description:"The new pattern."}))}),{description:"URL rewrite rules for static serving (e.g. SPA fallback). Only valid when serve is 'static'."})),run:s.Type.Optional(s.Type.Union([s.Type.Object({args:s.Type.Array(s.Type.String()),env:s.Type.Optional(s.Type.Record(s.Type.String(),s.Type.String()))},{additionalProperties:!1}),s.Type.String(),s.Type.Array(s.Type.String())],{description:"Command to run the service in production."})),serve:s.Type.Optional(s.Type.Union([s.Type.Literal("static"),s.Type.Literal("proxy")],{default:"proxy",description:"How the service is served in production. 'proxy' (default) proxies to a running process. 'static' serves files directly from publicDir."}))},{description:"Configuration for building and running the service in production."}))}))),title:s.Type.Optional(s.Type.String()),version:s.Type.Optional(s.Type.String())},{$id:"Artifact"});var u=e.i(357554),u=u,p=e.i(908796),c=e.i(973245),m=e.i(546180),y=e.i(566578);let h=c.gql`
    fragment ReplsTableRepl on Repl {
  ...ShadesReplCardRepl
  url
  timeCreated
  hostingDeployment {
    __typename
    ... on HostingDeployment {
      ...BuildStatusBadgeHostingDeployment
      currentBuild {
        id
        isPrivate
      }
    }
  }
}
    ${m.ShadesReplCardReplFragmentDoc}
${y.BuildStatusBadgeHostingDeploymentFragmentDoc}`;var g=e.i(951262),f=e.i(304277);e.i(566901);let T={},x=c.gql`
    mutation ReplsContainerUpdateRepl($input: UpdateReplInput!) {
  updateRepl(input: $input) {
    repl {
      id
      isStarred
    }
  }
}
    `,b=c.gql`
    mutation ReplsContainerToggleReplPin($input: ToggleReplPinInput!) {
  toggleReplPin(input: $input) {
    ... on Repl {
      id
      isCurrentUserStarred
    }
    ... on Error {
      message
    }
  }
}
    `,v=c.gql`
    query CurrentUserRepls($input: CurrentUserReplsInput!) {
  currentUser {
    id
    repls(input: $input) {
      __typename
      ... on ReplConnection {
        items {
          ...ReplsTableRepl
        }
        pageInfo {
          hasNextPage
          nextCursor
        }
      }
      ... on Error {
        message
      }
    }
  }
}
    ${h}`;var j=e.i(569910),S=e.i(619158),_=e.i(588992),w=e.i(320216),C=e.i(776065),R=e.i(330666),U=e.i(602686),P=e.i(36654),k=e.i(887964),F=e.i(943172),A=e.i(441503);let L={},I=c.gql`
    mutation ManageFoldersCreateFolder($name: String!, $parentId: String) {
  createReplFolder(name: $name, parentId: $parentId) {
    id
    name
    folderType
  }
}
    `,O=c.gql`
    mutation ManageFoldersUpdateFolder($folderId: String!, $name: String!) {
  updateReplFolder(folderId: $folderId, name: $name) {
    id
    name
  }
}
    `,M=c.gql`
    mutation ManageFoldersDeleteFolder($folderId: String!) {
  deleteReplFolder(folderId: $folderId) {
    id
  }
}
    `,D={},B=c.gql`
    query ReplsFiltersCreatorSearch($orgId: String!, $searchInput: OrgMembersInput!) {
  currentUser {
    id
    username
    fullName
    image
    org(orgId: $orgId) {
      __typename
      ... on Org {
        id
        members(input: $searchInput) {
          __typename
          ... on OrgMemberConnection {
            items {
              member {
                id
                user {
                  id
                  username
                  fullName
                  displayName
                  image
                }
              }
            }
          }
        }
      }
    }
  }
}
    `,E=c.gql`
    query ReplsFiltersFolderList {
  currentUser {
    id
    replFolder(id: "__ROOT_ID__") {
      id
      folders {
        id
        name
        folderType
        canEdit
      }
    }
  }
}
    `;function N(e){let t={...D,...e};return f.useQuery(E,t)}var V=e.i(183035),$=e.i(534141),q=e.i(302905),Q=e.i(491194),W=e.i(612343),z=e.i(643484),H=e.i(142406),K=e.i(488299),G=e.i(528710),J=e.i(528326),Y=e.i(8047),X=e.i(61732),Z=e.i(99170);function ee({isOpen:e,onClose:t,onFolderDeleted:r,refetchQueries:l=[]}){var i,s,o;let d,u,c,{showConfirm:m,showError:y}=(0,w.default)(),{data:h}=N({skip:!e}),f=(h?.currentUser?.replFolder?.folders??[]).filter(e=>e.folderType!==p.ReplFolderTypes.AllTeams),[T,x]=(0,n.useState)(""),[b,v]=(0,n.useState)(null),[j,S]=(0,n.useState)(null),[_,{loading:C}]=(i={refetchQueries:l},d={...L,...i},g.useMutation(I,d)),[R,{loading:U}]=(s={refetchQueries:l},u={...L,...s},g.useMutation(O,u)),[P,{loading:k}]=(o={refetchQueries:l},c={...L,...o},g.useMutation(M,c)),F=(0,n.useRef)(null),A=(0,n.useRef)(null),D=async()=>{let e=T.trim();if(e&&!C)try{await _({variables:{name:e}}),x(""),m("Folder created"),A.current?.focus()}catch(e){y(e instanceof Error?e.message:"Something went wrong when creating this folder")}},B=async()=>{if(!b||U)return;let e=b.name.trim();if(!e)return void v(null);try{await R({variables:{folderId:b.folderId,name:e}}),v(null),m("Folder renamed")}catch(e){y(e instanceof Error?e.message:"Something went wrong when renaming this folder")}},E=()=>{v(null)},et=async e=>{if(!k)try{await P({variables:{folderId:e}}),S(null),r?.(e),m("Folder deleted")}catch(e){y(e instanceof Error?e.message:"Something went wrong when deleting this folder")}};return(0,a.jsxs)(a.Fragment,{children:[(0,a.jsx)(J.Modal,{isOpen:e,onRequestClose:t,maxWidth:512,children:(0,a.jsxs)(X.View,{gap:24,children:[(0,a.jsx)(Y.Header,{level:3,variant:"headerDefault",children:"Manage Folders"}),(0,a.jsxs)(X.View,{gap:8,clsx:Z.default.folderList,children:[f.map(e=>(0,a.jsx)(X.View,{py:8,px:12,br:8,clsx:Z.default.folderRow,children:e.canEdit&&b?.folderId===e.id?(0,a.jsxs)(X.View,{row:!0,align:"center",gap:8,grow:!0,children:[(0,a.jsx)(q.default,{}),(0,a.jsx)(X.View,{grow:!0,children:(0,a.jsx)(G.Input,{value:b.name,onChange:e=>v({...b,name:e.target.value}),onKeyDown:e=>{"Enter"===e.key?B():"Escape"===e.key&&E()},onBlur:e=>{e.relatedTarget!==F.current&&E()},autoFocus:!0})}),(0,a.jsx)(K.IconButton,{ref:F,alt:"Save folder name",onClick:B,size:24,disabled:U,children:(0,a.jsx)(V.default,{})})]}):(0,a.jsxs)(X.View,{row:!0,align:"center",gap:8,grow:!0,clsx:Z.default.folderItem,children:[e.folderType===p.ReplFolderTypes.Multiplayer?(0,a.jsx)(W.default,{}):(0,a.jsx)(q.default,{}),(0,a.jsx)(Y.Text,{multiline:!1,clsx:Z.default.folderName,children:e.name}),e.canEdit?(0,a.jsxs)(X.View,{row:!0,gap:4,clsx:Z.default.folderActions,children:[(0,a.jsx)(K.IconButton,{alt:"Rename folder",onClick:()=>{v({folderId:e.id,name:e.name})},size:24,children:(0,a.jsx)($.default,{})}),(0,a.jsx)(K.IconButton,{alt:"Delete folder",colorway:"red",onClick:()=>S(e.id),size:24,children:(0,a.jsx)(Q.default,{})})]}):null]})},e.id)),0===f.length?(0,a.jsx)(X.View,{py:16,align:"center",children:(0,a.jsx)(Y.Text,{color:"dimmer",children:"No folders yet"})}):null]}),(0,a.jsxs)(X.View,{row:!0,gap:8,align:"center",children:[(0,a.jsx)(X.View,{grow:!0,children:(0,a.jsx)(G.Input,{ref:A,value:T,onChange:e=>x(e.target.value),onKeyDown:e=>{"Enter"===e.key&&D()},placeholder:"New folder name..."})}),(0,a.jsx)(z.Button,{colorway:"primary",text:"Add Folder",onClick:D,disabled:!T.trim()||C})]})]})}),(0,a.jsx)(J.Modal,{isOpen:null!==j,onRequestClose:()=>S(null),maxWidth:440,children:(0,a.jsx)(H.default,{prompt:"Delete folder?",desc:"Deleting this folder will also permanently delete all apps inside it. This action cannot be undone.",danger:!0,confirmText:"Delete folder",loading:k,onCancel:()=>S(null),onConfirm:()=>{j&&et(j)}})})]})}var et=e.i(167392),er=e.i(761201),el=e.i(66924),ea=e.i(480028),ei=e.i(919073),en=e.i(825419),es=e.i(585544),eo=e.i(295231),ed=e.i(658904),eu=e.i(189603);function ep({value:e,onChange:t,shouldIncludeDraft:r=!0}){let l=function(e){switch(e){case"success":return"Published";case"failed":return"Failed";case"not_deployed":return"Draft";default:return"Any status"}}(e),i=e??"any";return(0,a.jsxs)(eo.PopupMenu,{"aria-label":"Filter by publish status",trigger:(0,a.jsx)(z.Button,{variant:"nofill",text:l,iconRight:(0,a.jsx)(et.default,{}),clsx:eu.default.statusFilterButton}),selectionMode:"single",selectedKeys:new Set([i]),onSelectionChange:e=>{if("all"===e)return;let r=Array.from(e)[0];t("any"===r?void 0:r)},children:[(0,a.jsx)(eo.MenuItem,{id:"any",label:"Any status",iconRight:"any"===i?(0,a.jsx)(V.default,{}):null}),(0,a.jsx)(eo.MenuItem,{id:"success",label:"Published",iconRight:"success"===i?(0,a.jsx)(V.default,{}):null}),(0,a.jsx)(eo.MenuItem,{id:"failed",label:"Failed",iconRight:"failed"===i?(0,a.jsx)(V.default,{}):null}),r?(0,a.jsx)(eo.MenuItem,{id:"not_deployed",label:"Draft",iconRight:"not_deployed"===i?(0,a.jsx)(V.default,{}):null}):null]})}function ec({value:e,onChange:t}){let r=function(e){switch(e){case"public":return"Public";case"private":return"Private";default:return"Any access"}}(e),l=e??"any";return(0,a.jsxs)(eo.PopupMenu,{"aria-label":"Filter by access",trigger:(0,a.jsx)(z.Button,{variant:"nofill",text:r,iconRight:(0,a.jsx)(et.default,{}),clsx:eu.default.accessFilterButton}),selectionMode:"single",selectedKeys:new Set([l]),onSelectionChange:e=>{if("all"===e)return;let r=Array.from(e)[0];t("any"===r?void 0:r)},children:[(0,a.jsx)(eo.MenuItem,{id:"any",label:"Any access",iconRight:"any"===l?(0,a.jsx)(V.default,{}):null}),(0,a.jsx)(eo.MenuItem,{id:"public",label:"Public",iconRight:"public"===l?(0,a.jsx)(V.default,{}):null}),(0,a.jsx)(eo.MenuItem,{id:"private",label:"Private",iconRight:"private"===l?(0,a.jsx)(V.default,{}):null})]})}let em=[{label:"Design",kind:"design"},{label:"Web",kind:"web"},{label:"Data",kind:"data-app"},{label:"Mobile",kind:"mobile"},{label:"3D Game",kind:"game"}];function ey({value:e,onChange:t}){let r=function(e){if(!e)return"Any build type";let t=em.find(t=>t.kind===e);return t?.label??"Any build type"}(e),l=e??"any";return(0,a.jsxs)(eo.PopupMenu,{"aria-label":"Filter by build type",trigger:(0,a.jsx)(z.Button,{variant:"nofill",text:r,iconRight:(0,a.jsx)(et.default,{}),clsx:eu.default.buildTypeFilterButton}),selectionMode:"single",selectedKeys:new Set([l]),onSelectionChange:e=>{if("all"===e)return;let r=Array.from(e)[0];t("any"===r?void 0:r)},children:[(0,a.jsx)(eo.MenuItem,{id:"any",label:"Any build type",iconRight:"any"===l?(0,a.jsx)(V.default,{}):null}),em.map(e=>{let t=(0,el.getArtifactKindConfigFromString)(e.kind);return(0,a.jsx)(eo.MenuItem,{id:e.kind,label:e.label,icon:(0,a.jsx)(t.Icon,{size:16}),iconRight:l===e.kind?(0,a.jsx)(V.default,{}):null},e.kind)})]})}function eh({selectedUsers:e,onSelectedUsersChange:t,orgId:r,currentUserId:l}){var i;let s,[o,d]=(0,n.useState)(""),{data:u,loading:p}=(i={variables:{orgId:r,searchInput:{filters:{searchQuery:(0,S.default)(o,300)}}}},s={...D,...i},f.useQuery(B,s)),c=u?.currentUser,m=c?.username??"",y=c?.fullName??"",h=c?.image??"",g=(u?.currentUser?.org?.__typename==="Org"&&u.currentUser.org.members?.__typename==="OrgMemberConnection"?u.currentUser.org.members.items.map(e=>e.member.user):[]).filter(e=>e.id!==l).map(e=>({type:"member",id:e.id,displayName:e.displayName,fullName:e.fullName,username:e.username,image:e.image})),T=[{type:"me",id:l,label:"Created by me",fullName:y,username:m,image:h},...g],x=new Set(e);return(0,a.jsx)(ed.SearchableSelect,{"aria-label":"Filter by creator",selectedKeys:x,selectionMode:"multiple",onSelectionChange:e=>{"all"===e?t(new Set(T.map(e=>e.id))):t(e)},items:T,isLoading:p,clsx:eu.default.creatorList,trigger:(0,a.jsx)(z.Button,{variant:"nofill",text:function(e,t){let r=e.size;if(0===r)return"Any creator";if(1===r){let r=Array.from(e)[0],l=t.find(e=>e.id===r);return l?"me"===l.type?l.label:l.displayName:"1 creator"}return`${r} creators`}(e,T),iconRight:(0,a.jsx)(et.default,{}),clsx:eu.default.creatorFilterButton}),onInputChange:d,inputValue:o,children:e=>{let t=x.has(e.id);return"me"===e.type?(0,a.jsx)(es.BaseListBoxItem,{id:e.id,textValue:e.label,clsx:eu.default.creatorFilterItem,children:(0,a.jsxs)(ei.ShadesSurface,{row:!0,align:"center",gap:8,p:8,br:8,colorShade:"themeDefault",border:t?"strong":"subtle",elevate:"1x",grow:!0,clsx:eu.default.creatorMeSurface,children:[(0,a.jsx)(en.Avatar,{src:e.image,username:e.username,fullName:e.fullName}),(0,a.jsxs)(X.View,{grow:!0,clsx:eu.default.creatorItemContent,children:[(0,a.jsx)(es.ListBoxItemLabel,{children:e.label}),(0,a.jsxs)(es.ListBoxItemDescription,{children:["@",e.username]})]}),t?(0,a.jsx)(X.View,{shrink:0,children:(0,a.jsx)(V.default,{color:ea.tokens.accentPrimaryDefault,size:16})}):null]})},e.id):(0,a.jsx)(es.BaseListBoxItem,{id:e.id,textValue:e.displayName,clsx:eu.default.creatorFilterItem,children:(0,a.jsxs)(X.View,{row:!0,align:"center",gap:8,grow:!0,children:[(0,a.jsx)(en.Avatar,{src:e.image,username:e.username,fullName:e.fullName}),(0,a.jsxs)(X.View,{grow:!0,clsx:eu.default.creatorItemContent,children:[(0,a.jsx)(es.ListBoxItemLabel,{children:e.displayName}),(0,a.jsxs)(es.ListBoxItemDescription,{children:["@",e.username]})]}),t?(0,a.jsx)(X.View,{shrink:0,children:(0,a.jsx)(V.default,{size:16})}):null]})},e.id)}})}function eg({value:e,onChange:t,onManageFolders:r}){let l=`All ${er.REPL_DISPLAY_NAME.pluralLower}`,{data:i}=N(),n=(i?.currentUser?.replFolder?.folders??[]).filter(e=>e.folderType!==p.ReplFolderTypes.AllTeams),s=n.find(t=>t.id===e),o=s?.name??l,d=e??"all";return(0,a.jsxs)(eo.PopupMenu,{"aria-label":"Filter by folder",trigger:(0,a.jsx)(z.Button,{variant:"outlined",text:o,iconLeft:s?.folderType===p.ReplFolderTypes.Multiplayer?(0,a.jsx)(W.default,{}):(0,a.jsx)(q.default,{}),iconRight:(0,a.jsx)(et.default,{}),alignment:"start",clsx:eu.default.folderFilterButton}),selectionMode:"single",selectedKeys:new Set([d]),onSelectionChange:e=>{if("all"===e)return;let l=Array.from(e)[0];"manage"===l?r():t("all"===l?void 0:l)},children:[(0,a.jsx)(eo.MenuItem,{id:"all",label:l,icon:(0,a.jsx)(q.default,{}),iconRight:"all"===d?(0,a.jsx)(V.default,{}):null}),n.map(e=>(0,a.jsx)(eo.MenuItem,{id:e.id,label:e.name,icon:e.folderType===p.ReplFolderTypes.Multiplayer?(0,a.jsx)(W.default,{}):(0,a.jsx)(q.default,{}),iconRight:d===e.id?(0,a.jsx)(V.default,{}):null},e.id)),(0,a.jsx)(eo.Separator,{}),(0,a.jsx)(eo.MenuItem,{id:"manage",label:"Manage folders"})]})}var ef=e.i(62674),eT=e.i(443588),ex=e.i(802684);function eb({items:e,trackingContext:t,loading:r,errorMessage:l,canLoadMore:i,onLoadMore:n,isOrg:s,hasActiveFilters:o,onTogglePin:d,hideDelete:u,shouldShowPublishedArtifactsOnly:p}){let c=er.REPL_DISPLAY_NAME.plural;if(l)return(0,a.jsx)(X.View,{align:"center",justify:"center",p:32,children:(0,a.jsx)(Y.Text,{children:l})});if(0===e.length&&!r){let e;return e=o?`Try adjusting or clearing your filters to see all ${c}`:`Create a ${er.REPL_DISPLAY_NAME.singular} to get started`,(0,a.jsxs)(X.View,{align:"center",justify:"center",p:32,gap:8,children:[(0,a.jsx)(ef.default,{size:24}),(0,a.jsx)(Y.Text,{children:o?`No matching ${c}`:`No ${c} yet`}),(0,a.jsx)(Y.Text,{variant:"small",color:"dimmer",children:e})]})}return 0===e.length&&r?(0,a.jsx)(X.View,{clsx:ex.default.grid,children:Array.from({length:8}).map((e,t)=>(0,a.jsx)(ei.ShadesSurface,{border:"subtle",br:"container",clsx:ex.default.cardSkeleton},t))}):(0,a.jsxs)(X.View,{children:[(0,a.jsx)(X.View,{clsx:ex.default.grid,tag:"ol",children:e.map(e=>(0,a.jsx)(eT.ReplCard,{repl:e,trackingContext:t,isOrg:s,showPinBadge:!0,onTogglePin:d,hideDelete:u,shouldShowPublishedArtifactsOnly:p,showLastOpened:!0},e.id))}),i?(0,a.jsx)(X.View,{align:"center",py:16,children:(0,a.jsx)(z.Button,{onClick:n,disabled:r,variant:"outlined",text:r?"Loading...":"Load more"})}):null]})}var ev=e.i(413974),ej=e.i(757053),eS=e.i(857619),e_=e.i(453891),ew=e.i(775007),eC=e.i(609912),eR=e.i(984119),eU=e.i(508454),eP=e.i(472499),ek=e.i(21875),eF=e.i(519425),eA=e.i(365757),eL=e.i(710596);let eI={selector:{id:"selector",key:"selector",label:"",width:36,minWidth:36},title:{id:"title",key:"title",label:"Name",isRowHeader:!0,minWidth:150},creator:{id:"creator",key:"creator",label:"Creator",width:200},access:{id:"access",key:"access",label:"Access",width:100},lastUpdated:{id:"lastUpdated",key:"lastUpdated",label:"Last updated",allowSorting:!0,width:150},createdAt:{id:"createdAt",key:"createdAt",label:"Created",allowSorting:!0,width:150},publishedUrl:{id:"publishedUrl",key:"publishedUrl",label:"Published URL",width:250},publishedStatus:{id:"publishedStatus",key:"publishedStatus",label:"Published status",width:150},publishedAt:{id:"publishedAt",key:"publishedAt",label:"Published at",allowSorting:!0,width:150},actions:{id:"actions",key:"actions",label:"",width:48}};function eO({deployment:e}){let t=e?.__typename==="HostingDeployment"?e:null,{href:r,displayUrl:l}=(0,e_.useDeploymentLink)(t);return r?(0,a.jsx)(eR.TableCell,{children:(0,a.jsx)("a",{href:r,target:"_blank",rel:"noopener noreferrer",onClick:e=>e.stopPropagation(),children:(0,a.jsx)(Y.Text,{variant:"small",color:"dimmer",multiline:!1,children:l})})},"publishedUrl"):(0,a.jsx)(eR.TableCell,{},"publishedUrl")}function eM({repl:e,onTogglePin:r}){let l=(0,t.useFlag)({controlName:"flag-per-user-pinning"});return e.authorizations.star.isAuthorized&&(l?e.isCurrentUserStarred:e.isStarred)?(0,a.jsx)(eR.TableCell,{children:(0,a.jsx)(K.IconButton,{alt:"Unpin from top",size:24,onClick:()=>r(e.id,!1),children:(0,a.jsx)(ej.default,{size:16})})},"selector"):(0,a.jsx)(eR.TableCell,{},"selector")}function eD({columns:e,items:t,loading:r,canLoadMore:l,onLoadMore:i,errorMessage:n,onSortChange:s,trackingContext:o,onTogglePin:d,hasActiveFilters:u,hideDelete:p}){let c=er.REPL_DISPLAY_NAME.plural,m=e.map(e=>{let t=eI[e];return"lastUpdated"===e?{...t,label:"Last opened"}:t});return(0,a.jsx)(X.View,{gap:32,clsx:eL.default.wrapper,children:(0,a.jsx)(ei.ShadesSurface,{row:!0,justify:"space-between",clsx:eL.default.tableWrapper,elevate:!1,children:(0,a.jsx)(eC.IndexTable,{title:c,clsx:eL.default.table,autoLayout:!1,tableProps:{style:{tableLayout:"fixed",borderCollapse:"separate"},disabledBehavior:"all"},columns:m,items:t,loading:r,loadingPlaceholder:{numRows:25,height:36},errorMessage:n,emptyState:(0,a.jsx)(ew.default,{title:r?`Loading ${c}\u2026`:u?`No matching ${c}`:`No ${c} yet`,description:(()=>{if(!r)return u?`Try adjusting or clearing your filters to see all ${c}`:`Create a ${er.REPL_DISPLAY_NAME.singular} to get started`})(),illustration:(0,a.jsx)(ef.default,{size:24})}),canLoadMore:l,onLoadMore:i,onSortChange:s,isLoadingMore:t.length>0&&r,children:t=>(0,a.jsx)(eU.TableRow,{id:t.id,href:t.url,children:e.map(e=>(function(e,t,r,l,i){switch(e){case"selector":return(0,a.jsx)(eM,{repl:t,onTogglePin:l},"selector");case"title":return(0,a.jsx)(eR.TableCell,{children:(0,a.jsxs)(X.View,{row:!0,gap:8,align:"center",clsx:eL.default.titleCell,children:[(0,a.jsx)(eA.default,{iconUrl:t.iconUrl??"",size:20,alt:t.title}),(0,a.jsx)(Y.Text,{clsx:eL.default.titleText,children:t.title})]})},"title");case"creator":return(0,a.jsx)(eR.TableCell,{children:t.user?(0,a.jsx)(ev.default,{href:`/@${t.user.username}`,onClick:e=>e.stopPropagation(),children:(0,a.jsx)(ek.User,{src:t.user.image,username:t.user.username,fullName:t.user.fullName,small:!0})}):null},"creator");case"access":return(0,a.jsx)(eR.TableCell,{children:(0,a.jsx)(Y.Text,{variant:"small",color:"dimmer",children:t.isPrivate?"Private":"Public"})},"access");case"publishedUrl":return(0,a.jsx)(eO,{deployment:t.hostingDeployment});case"lastUpdated":{let e=t.lastOpened??null;return(0,a.jsx)(eR.TableCell,{children:e?(0,a.jsx)(eP.Timestamp,{textVariant:"small",textColor:"dimmer",dateFormat:"relative",date:e}):(0,a.jsx)(Y.Text,{variant:"small",color:"dimmest",children:"—"})},"lastUpdated")}case"createdAt":return(0,a.jsx)(eR.TableCell,{children:(0,a.jsx)(eP.Timestamp,{textVariant:"small",textColor:"dimmer",dateFormat:"relative",date:t.timeCreated})},"createdAt");case"publishedStatus":{let e=t.hostingDeployment?.__typename==="HostingDeployment"?t.hostingDeployment:null;return(0,a.jsx)(eR.TableCell,{children:e?(0,a.jsx)(eS.BuildStatusesBadge,{deployment:e}):(0,a.jsx)(Y.Text,{color:"dimmest",multiline:!1,children:"Draft"})},"publishedStatus")}case"publishedAt":{let e=t.hostingDeployment?.__typename==="HostingDeployment"?t.hostingDeployment.currentBuild.timeCreated:null;if(!e)return(0,a.jsx)(eR.TableCell,{},"publishedAt");return(0,a.jsx)(eR.TableCell,{children:(0,a.jsx)(eP.Timestamp,{textVariant:"small",textColor:"dimmer",dateFormat:"relative",date:e})},"publishedAt")}case"actions":return(0,a.jsx)(eR.TableCell,{layout:"floatRight",children:(0,a.jsx)(eF.ReplActions,{repl:t,trackingContext:r,deleteAction:i?{type:"hidden"}:void 0})},"actions")}})(e,t,o,d,p))})})})})}var eB=e.i(449525),eE=e.i(419635),eN=e.i(97043),eV=e.i(117964);function e$({columns:e,items:t,loading:r,canLoadMore:l,onLoadMore:i,errorMessage:s,onSortChange:o,header:d,searchValue:u,onSearchChange:p,onSearchCommit:c,filters:m,onFilterChange:y,hasAppliedState:h,hasActiveFilters:g,onClearAll:f,orgId:T,currentUserId:x,showDraftOption:b=!0,activeView:v,onViewChange:S,trackingContext:_,isOrg:w,onTogglePin:C,onFolderDeleted:A,orgSlug:L,canDownloadCsv:I=!1,hideDelete:O,shouldShowPublishedArtifactsOnly:M}){let[D,B]=(0,n.useState)(!1),E=m.find(e=>"folder"===e.type),N=m.filter(e=>"folder"!==e.type);return(0,a.jsxs)(X.View,{clsx:eV.default.container,children:[(0,a.jsxs)(X.View,{row:!0,align:"center",gap:8,pb:16,children:[(0,a.jsx)(F.default,{size:24}),(0,a.jsx)(Y.Header,{level:1,variant:"headerDefault",children:d})]}),(0,a.jsxs)(X.View,{row:!0,wrap:!0,justify:"space-between",align:"center",gap:8,pb:16,clsx:eV.default.filterBar,children:[(0,a.jsxs)(X.View,{row:!0,gap:8,align:"center",wrap:!0,children:[(0,a.jsx)(X.View,{grow:!0,clsx:eV.default.searchBarWrapper,children:(0,a.jsx)(eN.SearchBar,{value:u,onChange:e=>p(e.target.value),onClear:()=>{p(""),c("")},onBlur:()=>c(u),onKeyDown:e=>{"Enter"===e.key&&c(u)},placeholder:"Search"})}),N.map(e=>{switch(e.type){case"publishedStatus":return(0,a.jsx)(ep,{value:e.value,onChange:e=>y({type:"publishedStatus",value:e}),shouldIncludeDraft:b},e.type);case"access":return(0,a.jsx)(ec,{value:e.value,onChange:e=>y({type:"access",value:e})},e.type);case"buildType":return(0,a.jsx)(ey,{value:e.value,onChange:e=>y({type:"buildType",value:e})},e.type);case"creator":if(!T||void 0===x)return null;return(0,a.jsx)(eh,{selectedUsers:e.value,onSelectedUsersChange:e=>y({type:"creator",value:e}),orgId:T,currentUserId:x},e.type);default:(0,j.default)(e)}}),h?(0,a.jsx)(z.Button,{variant:"nofill",iconLeft:(0,a.jsx)(U.default,{}),"aria-label":"Clear all filters",text:"",onClick:f}):null]}),(0,a.jsxs)(X.View,{row:!0,gap:8,align:"center",children:[I&&L?(0,a.jsx)(eE.ButtonLink,{text:"Download CSV",iconLeft:(0,a.jsx)(P.default,{}),href:{pathname:`/t/${L}/apps.csv`},target:"_blank",download:!0}):null,E?(0,a.jsx)(eg,{value:E.value,onChange:e=>y({type:"folder",value:e}),onManageFolders:()=>B(!0)}):null,(0,a.jsx)(X.View,{clsx:eV.default.viewSwitcher,children:(0,a.jsxs)(eB.ButtonGroup,{row:!0,name:"viewFilter",value:v,onChange:S,children:[(0,a.jsx)(eB.ButtonGroupItem,{id:"grid",icon:(0,a.jsx)(F.default,{}),value:"grid",text:(0,a.jsx)(R.VisuallyHidden,{children:"Grid view"})}),(0,a.jsx)(eB.ButtonGroupItem,{id:"table",icon:(0,a.jsx)(k.default,{}),value:"table",text:(0,a.jsx)(R.VisuallyHidden,{children:"Table view"})})]})})]})]}),(0,a.jsx)(eq,{orgId:"grid"===v&&t.length>0?T:void 0,children:"grid"===v?(0,a.jsx)(eb,{items:t,trackingContext:_,loading:r,errorMessage:s,canLoadMore:l,onLoadMore:i,isOrg:w,hasActiveFilters:g,onTogglePin:C,hideDelete:O,shouldShowPublishedArtifactsOnly:M}):(0,a.jsx)(eD,{columns:e,items:t,loading:r,canLoadMore:l,onLoadMore:i,errorMessage:s,onSortChange:o,trackingContext:_,onTogglePin:C,hasActiveFilters:g,hideDelete:O})}),(0,a.jsx)(ee,{isOpen:D,onClose:()=>B(!1),onFolderDeleted:A,refetchQueries:["ReplsFiltersFolderList","CurrentUserRepls"]})]})}function eq({orgId:e,children:t}){return e?(0,a.jsx)(A.ReplPresenceProvider,{orgId:e,children:t},e):t}let eQ=s.Type.Union([s.Type.Literal(p.CurrentUserReplsSortTypeEnum.CreationDate),s.Type.Literal(p.CurrentUserReplsSortTypeEnum.LastOpened),s.Type.Literal(p.CurrentUserReplsSortTypeEnum.LastUpdated),s.Type.Literal(p.CurrentUserReplsSortTypeEnum.PublishedAt)]),eW=s.Type.Union([s.Type.Literal(p.CurrentUserReplsSortDirectionEnum.Ascending),s.Type.Literal(p.CurrentUserReplsSortDirectionEnum.Descending)]),ez=s.Type.Union([s.Type.Literal(p.CurrentUserReplsDeploymentStatusEnum.Deployed),s.Type.Literal(p.CurrentUserReplsDeploymentStatusEnum.Failed),s.Type.Literal(p.CurrentUserReplsDeploymentStatusEnum.NotDeployed),s.Type.Literal(p.CurrentUserReplsDeploymentStatusEnum.Success)]),eH=s.Type.Union([s.Type.Literal(p.CurrentUserReplsVisibilityEnum.Private),s.Type.Literal(p.CurrentUserReplsVisibilityEnum.Public)]),eK=s.Type.Union([s.Type.Literal("grid"),s.Type.Literal("table")]),eG=s.Type.Union([s.Type.Literal("__MULTIPLAYER_REPLS__"),s.Type.String({pattern:"^__TEAM__\\d+__$"})]),eJ={lastUpdated:p.CurrentUserReplsSortTypeEnum.LastOpened,createdAt:p.CurrentUserReplsSortTypeEnum.CreationDate,publishedAt:p.CurrentUserReplsSortTypeEnum.PublishedAt};function eY({sortType:e,sortDirection:t,defaultSortType:r=p.CurrentUserReplsSortTypeEnum.LastUpdated}){return{sortType:e??r,direction:t??p.CurrentUserReplsSortDirectionEnum.Descending,pinnedFirst:!0}}function eX({orgId:e,publishedOnly:t,sort:r,cursor:l,search:a,filters:i}){let n={},s=!1;for(let e of i)switch(e.type){case"publishedStatus":e.value&&(n.deploymentStatus=e.value,s=!0);break;case"access":e.value&&(n.visibility=e.value);break;case"creator":e.value.size>0&&(n.createdBy={userIds:Array.from(e.value)});break;case"folder":e.value&&(n.folderId=e.value);break;case"buildType":e.value&&(n.artifactKind=e.value);break;default:(0,j.default)(e)}return!s&&t&&(n.deploymentStatus=p.CurrentUserReplsDeploymentStatusEnum.Deployed),{count:25,sort:r,cursor:l,...e?{orgId:e}:{},...a?{search:a}:{},...Object.keys(n).length>0?{filters:n}:{}}}e.s(["ReplsContainer",0,function({orgId:e,publishedOnly:r=!1,columns:l,availableFilters:s,header:c,trackingContext:m,orgSlug:y,canDownloadCsv:h=!1}){var R;let U,P,k,F,A,L,I,O,M,D,B,E,N=(0,i.useRouter)(),{showError:V}=(0,w.default)(),$=s.includes("buildType")?s:[...s,"buildType"],{sortType:q,sortDirection:Q,search:W,statusFilter:z,accessFilter:H,selectedCreators:K,view:G,folderFilter:J,buildTypeFilter:Y}=(U=(0,C.useQueryParam)("sort","string"),P=(0,C.useQueryParam)("order","string"),k=(0,C.useQueryParam)("search","string"),F=(0,C.useQueryParam)("status","string"),A=(0,C.useQueryParam)("access","string"),L=(0,C.useQueryParam)("creator","string"),I=(0,C.useQueryParam)("view","string"),O=(0,C.useQueryParam)("folder","string"),M=(0,C.useQueryParam)("buildType","string"),(0,n.useMemo)(()=>{let e=o.Value.Check(eQ,U)?U:void 0,t=o.Value.Check(eW,P)?P:void 0,r=o.Value.Check(ez,F)?F:void 0,l=o.Value.Check(eH,A)?A:void 0,a=new Set;L&&L.split(",").filter(Boolean).map(Number).filter(e=>!Number.isNaN(e)&&e>0).forEach(e=>a.add(e));let i=o.Value.Check(eK,I)?I:void 0;return{sortType:e,sortDirection:t,search:k,statusFilter:r,accessFilter:l,selectedCreators:a,view:i,folderFilter:O&&((0,u.default)(O)||o.Value.Check(eG,O))?O:void 0,buildTypeFilter:o.Value.Check(d.properties.kind,M)?M:void 0}},[U,P,k,F,A,L,I,O,M])),[X,Z]=(0,_.default)("repls-view-mode","grid"),ee=p.CurrentUserReplsSortTypeEnum.LastOpened,et=eY({sortType:q,sortDirection:Q,defaultSortType:ee}),[er,el]=(0,n.useState)(W??""),ea=(0,S.default)(er,250);(0,n.useEffect)(()=>{el(W??"")},[W]);let ei=$.map(e=>{switch(e){case"publishedStatus":return{type:"publishedStatus",value:z};case"access":return{type:"access",value:H};case"creator":return{type:"creator",value:K};case"folder":return{type:"folder",value:J};case"buildType":return{type:"buildType",value:Y};default:(0,j.default)(e)}}),en=!!(er||ei.some(e=>{switch(e.type){case"publishedStatus":case"access":case"buildType":case"folder":return void 0!==e.value;case"creator":return e.value.size>0;default:(0,j.default)(e)}})),es=en||!!q,{data:eo,previousData:ed,loading:eu,error:ep,fetchMore:ec}=(R={refetchWritePolicy:"overwrite",fetchPolicy:"cache-and-network",nextFetchPolicy:"cache-first",notifyOnNetworkStatusChange:!0,ssr:!1,variables:{input:eX({orgId:e,publishedOnly:r,sort:et,cursor:void 0,search:ea||void 0,filters:ei})}},D={...T,...R},f.useQuery(v,D)),em=eo?.currentUser?.repls?.__typename==="ReplConnection"?eo.currentUser.repls:void 0,ey=em?.items??[],eh=eo?.currentUser?.id??ed?.currentUser?.id,eg=em?.pageInfo.hasNextPage??!1,ef=ep?.message,eT=eo?.currentUser?.repls?.__typename==="NotFoundError"||eo?.currentUser?.repls?.__typename==="UserError"?eo.currentUser.repls.message:void 0,ex=(0,n.useCallback)(async()=>{if(eu||!em?.pageInfo.nextCursor)return;let t=eX({orgId:e,publishedOnly:r,sort:eY({sortType:q,sortDirection:Q,defaultSortType:ee}),cursor:em.pageInfo.nextCursor,search:ea||void 0,filters:ei});await ec({variables:{input:t},updateQuery:(e,{fetchMoreResult:t})=>{if(t.currentUser?.repls?.__typename!=="ReplConnection")return V("Could not load more results - please refresh the page and try again"),e;let r=[...e.currentUser?.repls?.__typename==="ReplConnection"?e.currentUser.repls.items:[],...t.currentUser.repls.items];return{...t,currentUser:{...t.currentUser,repls:{...t.currentUser.repls,items:r}}}}})},[eu,ec,e,r,q,Q,ee,ea,ei,em?.pageInfo.nextCursor,V]),eb=(0,t.useFlag)({controlName:"flag-per-user-pinning"}),[ev,{loading:ej}]=(B={...T,...void 0},g.useMutation(x,B)),[eS,{loading:e_}]=(E={...T,...void 0},g.useMutation(b,E)),ew=ej||e_,eC=(0,n.useCallback)((e,t)=>{ew||(eb?eS({variables:{input:{replId:e,pinned:t}},optimisticResponse:{__typename:"RootMutationType",toggleReplPin:{__typename:"Repl",id:e,isCurrentUserStarred:t}},refetchQueries:["CurrentUserRepls"],onCompleted:e=>{let t=e.toggleReplPin;t&&"message"in t&&V(t.message)},onError:e=>{V(e.message)}}):ev({variables:{input:{id:e,isStarred:t}},optimisticResponse:{__typename:"RootMutationType",updateRepl:{__typename:"UpdateReplPayload",repl:{__typename:"Repl",id:e,isStarred:t}}},refetchQueries:["CurrentUserRepls"],onError:e=>{V(e.message)}}))},[ev,eS,ew,eb,V]),eR=(0,n.useCallback)(e=>{J===e&&(0,C.updatePathWithQueryParams)({router:N,params:[{mode:"delete",key:"folder"}]})},[J,N]);return(0,a.jsx)(e$,{columns:l,items:ey,loading:eu,canLoadMore:eg,onLoadMore:ex,errorMessage:ef??eT,onSortChange:e=>{let t=eJ[String(e.column)];t&&(0,C.updatePathWithQueryParams)({router:N,params:[{mode:"add",key:"sort",value:t},{mode:"add",key:"order",value:"ascending"===e.direction?p.CurrentUserReplsSortDirectionEnum.Ascending:p.CurrentUserReplsSortDirectionEnum.Descending}]})},header:c,searchValue:er,onSearchChange:e=>{el(e)},onSearchCommit:e=>{(0,C.updatePathWithQueryParams)({router:N,params:e?[{mode:"add",key:"search",value:e}]:[{mode:"delete",key:"search"}]})},filters:ei,onFilterChange:e=>{switch(e.type){case"publishedStatus":{let t="status";(0,C.updatePathWithQueryParams)({router:N,params:e.value?[{mode:"add",key:t,value:e.value}]:[{mode:"delete",key:t}]});break}case"access":(0,C.updatePathWithQueryParams)({router:N,params:e.value?[{mode:"add",key:"access",value:e.value}]:[{mode:"delete",key:"access"}]});break;case"creator":(0,C.updatePathWithQueryParams)({router:N,params:e.value.size>0?[{mode:"add",key:"creator",value:Array.from(e.value).join(",")}]:[{mode:"delete",key:"creator"}]});break;case"folder":(0,C.updatePathWithQueryParams)({router:N,params:e.value?[{mode:"add",key:"folder",value:e.value}]:[{mode:"delete",key:"folder"}]});break;case"buildType":(0,C.updatePathWithQueryParams)({router:N,params:e.value?[{mode:"add",key:"buildType",value:e.value}]:[{mode:"delete",key:"buildType"}]});break;default:(0,j.default)(e)}},hasAppliedState:es,hasActiveFilters:en,onClearAll:()=>{el(""),(0,C.updatePathWithQueryParams)({router:N,params:[{mode:"delete",key:"search"},{mode:"delete",key:"status"},{mode:"delete",key:"access"},{mode:"delete",key:"creator"},{mode:"delete",key:"sort"},{mode:"delete",key:"buildType"},{mode:"delete",key:"order"},{mode:"delete",key:"folder"}]})},showDraftOption:!r,orgId:e,currentUserId:eh,activeView:G??X,onViewChange:e=>{Z(e),(0,C.updatePathWithQueryParams)({router:N,params:[{mode:"add",key:"view",value:e}]})},trackingContext:m,isOrg:!!e,onTogglePin:eC,onFolderDeleted:eR,orgSlug:y,canDownloadCsv:h,hideDelete:r,shouldShowPublishedArtifactsOnly:r})}],56268)}]);

//# debugId=e4c27179-9ebb-2c72-40d7-e6d5d12c4d57
//# sourceMappingURL=0b-t1p_s1d~w2.js.map
